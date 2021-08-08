from datetime import datetime, timedelta, date
from typing import List, Tuple, Dict, Optional

from server.extentions import db

DateCycleEvent = db.Table(
    'date_cycle_event',
    db.Column(
        'date_id', db.Integer, db.ForeignKey('date.id'), primary_key=True),
    db.Column(
        'cycleevent_id', db.Integer, db.ForeignKey('cycleevent.id'),
        primary_key=True)
)


class Date(db.Model):
    __tablename__ = 'date'
    id = db.Column(db.Integer, primary_key=True)
    date_ = db.Column(db.Date, unique=True, index=True)
    cycle_event = db.relationship(
        'CycleEvent', secondary='date_cycle_event', back_populates='date_')

    @classmethod
    def set_date(
            cls, new_date: date, event_type: str = 'cycle_start'
    ) -> None:
        """
        Create Date instance for new_date, create relation with event_type,
        commit to DB.
        """
        date_to_set = cls(date_=new_date)
        event = CycleEvent.query.filter(CycleEvent.type_ == event_type).first()
        date_to_set.cycle_event.append(event)
        db.session.add(date_to_set)
        db.session.commit()

    @staticmethod
    def _get_or_create(date_: datetime.date):
        # ToDo: does it need???
        date_inst = Date.query.filter(Date.date_ == date_).first()
        if date_inst:
            return date_inst
        else:
            date_inst = Date(date_=date_)
            db.session.add(date_inst)
            return date_inst

    @classmethod
    def get_dates(
            cls,
            event_type: Optional[str] = None
    ) -> List['Date']:
        """
        Get all Date instances witch are related to
        CycleEvent instance with type_ =  event_type.
        Sort in ascending order by date_ field

        """
        if event_type:
            dates = cls.query.join(Date.cycle_event) \
                .filter(CycleEvent.type_ == event_type) \
                .order_by(cls.date_.asc()).all()
        else:
            dates = cls.query.order_by(cls.date_.asc()).all()
        return dates

    def __repr__(self):
        return f'date {self.date_}'


class CycleEvent(db.Model):
    __tablename__ = 'cycleevent'
    id = db.Column(db.Integer, primary_key=True)
    type_ = db.Column(db.String(30), unique=True, index=True)
    date_ = db.relationship(
        'Date', secondary='date_cycle_event', back_populates='cycle_event')

    @classmethod
    def get_by_type(cls, type_to_get):
        inst = cls.query.filter(cls.type_ == type_to_get).first()
        return inst

    @classmethod
    def repr_from_list(cls, instances: List['CycleEvent']) -> List[str]:
        """"""
        res = [inst.type_ for inst in instances]
        return res

    @classmethod
    def remove_date_from_start_cycle(cls, date_to_remove: date) -> None:
        """"""
        event_type = 'cycle_start'
        date_inst_to_remove = Date.query.filter(Date.date_ == date_to_remove).first()
        event = cls.query.filter(cls.type_ == event_type).first()
        event.date_.remove(date_inst_to_remove)
        db.session.commit()

    def __repr__(self):
        return f'cycle event {self.type_}'


