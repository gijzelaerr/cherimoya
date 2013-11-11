import os
from flask import Flask
from flask.ext.assets import Environment
from webassets.loaders import PythonLoader
from cherimoya import views
from cherimoya import db

app = Flask(__name__)
app.config.from_object('cherimoya.default_settings')

if 'CHERIMOYA_SETTINGS' in os.environ:
    app.config.from_envvar('CHERIMOYA_SETTINGS')
else:
    app.config.from_pyfile('settings.cfg')

# Database init
db.db.init_app(app)

# Assets init
asset_env = Environment()
asset_mod_name = __name__.split(".")[0] + ".assets"
for name, bundle in PythonLoader(asset_mod_name).load_bundles().iteritems():
    asset_env.register(name, bundle)
asset_env.init_app(application)

# Routing init
for route in views.routes:
    app.add_url_rule(route[0], route[1], route[2], methods=route[3])

if __name__ == '__main__':
    app.run()
