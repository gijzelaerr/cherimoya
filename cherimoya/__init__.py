import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from cherimoya import views
from cherimoya import db
from cherimoya import assets
from cherimoya import views
from cherimoya.assets import main_styles, main_scripts


app = Flask(__name__)
app.config.from_object('cherimoya.default_settings')


if 'CHERIMOYA_SETTINGS' in os.environ:
    app.config.from_envvar('CHERIMOYA_SETTINGS')
else:
    app.config.from_pyfile('settings.cfg')

db.db.app = app
db.db.init_app(app)
assets.init_app(app)
views.init_app(app)
toolbar = DebugToolbarExtension(app)


if __name__ == '__main__':
    app.run()
