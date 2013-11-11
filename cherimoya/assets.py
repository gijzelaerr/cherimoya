from webassets import Bundle

main_styles = Bundle(
    "styles/normalize.css",
    "styles/main.css",
    filters=["cssmin"],
    output="cached_styles/main.css"
)

main_scripts = Bundle(
    "scripts/jquery-1.8.0.js",
    filters=["jsmin"],
    output="cached_scripts/main.js"
)