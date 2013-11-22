from webassets import Bundle
from flask.ext.assets import Environment

main_styles = Bundle(
    'js/bootstrap/css/bootstrap.css',
    filters=["cssmin"],
    output="cached_styles/main.css"
)

main_scripts = Bundle(
    'js/jquery/jquery.min.js',
    'js/bootstrap/js/bootstrap.min.js',
    'js/d3/d3.min.js',
    'js/highcharts/highcharts.js',
    filters='jsmin',
    output='cached_scripts/main.js'
)

def init_app(app):
    assets = Environment(app)
    assets.register('main_styles', main_styles)
    assets.register('main_scripts', main_scripts)