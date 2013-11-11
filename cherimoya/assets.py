from webassets import Bundle

main_styles = Bundle(
    'js/bootstrap/css/bootstrap.css',
    filters=["cssmin"],
    output="cached_styles/main.css"
)

main_scripts = Bundle(
    'js/jquery/jquery.min.js',
    'js/bootstrap/js/bootstrap.min.js',
    'js/d3/d3.min.js',
    filters='jsmin',
    output='cached_scripts/main.js'
)