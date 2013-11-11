import os
from flask import Flask
from flask.ext.assets import Environment, Bundle
from cherimoya import views
from cherimoya import db
from cherimoya.assets import main_styles, main_scripts

app = Flask(__name__)
app.config.from_object('cherimoya.default_settings')

if 'CHERIMOYA_SETTINGS' in os.environ:
    app.config.from_envvar('CHERIMOYA_SETTINGS')
else:
    app.config.from_pyfile('settings.cfg')

# Database init
db.db.init_app(app)

# init assets
assets = Environment(app)
assets.register('main_styles', main_styles)
assets.register('main_scripts', main_scripts)

# Routing init
for route in views.routes:
    app.add_url_rule(route[0], route[1], route[2], methods=route[3])

if __name__ == '__main__':
    app.run()
