from flask import render_template
from cherimoya.db import Statistic


def index():
    statistics = Statistic.query.order_by(Statistic.name).all()
    return render_template('index.html', statistics=statistics)

routes = [
    ("/", "index", index, ["GET"])
]


def init_app(app):
    for route in routes:
        app.add_url_rule(route[0], route[1], route[2], methods=route[3])