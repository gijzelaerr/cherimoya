from flask import render_template
from cherimoya.db import Statistic


def index():
    statistics = Statistic.query.order_by(Statistic.name).all()
    return render_template('index.html', statistics=statistics)

routes = [
    ("/", "index", index, ["GET"])
]

