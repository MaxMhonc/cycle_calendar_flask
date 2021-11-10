from config import Config
from server.extentions import app, db, migrate
from server.views import home_page
from server.api import api
from server.models import Date, CycleEvent

app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(home_page)
app.register_blueprint(api)


@app.shell_context_processor
def make_shell_context():
    from datetime import date
    return {'db': db, 'Date': Date, 'CycleEvent': CycleEvent, 'date': date}


if __name__ == '__main__':
    # ToDo: remove it
    # test new ssh connection
    app.run()
