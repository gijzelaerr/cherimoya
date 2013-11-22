from flask import render_template, url_for
from cherimoya.db import Statistic, Line, db, type_map


def index():
    x = url_for('index')
    statistics = Statistic.query.order_by(Statistic.name).all()
    return render_template('index.html', statistics=statistics)


def value_index_count(value, stat_name):
    """
    :param value: one of the cherimoya.db.*Value objects
    :param stat_name: the name of the statistic
    """
    return db.session.query(value.index).\
        filter(Line.statistic_id == Statistic.id,
               value.line_id == Line.id,
               Statistic.name == stat_name).\
        distinct(value.index).count()


def index_count(stat_name):
    return {t: value_index_count(v, stat_name) for (t, v) in type_map.items()}


def plot(name, type_, index_):
    assert type_ in type_map.keys()
    Value = type_map[type_]
    series = Value.query.\
        filter(Value.line_id == Line.id,
               Line.statistic_id == Statistic.id,
               Statistic.name == name,
               Value.index == index_).\
        order_by(Line.moment).all()
    return render_template(type_ +'.html', series=series, name=name,
                           index_=index_, type_=type_)


def statistic(name):
    stat = Statistic.query.filter(Statistic.name == name).first_or_404()
    indexes = index_count(name)
    return render_template('statistic.html', statistic=stat, indexes=indexes)


def line(id):
    l = Line.query.filter(Line.id == id).first_or_404()
    return render_template('line.html', line=line)


routes = [
    ("/", "index", index, ["GET"]),
    ("/statistic/<name>/", "statistic", statistic, ["GET"]),
    ("/line/<int:id>/", "line", line, ["GET"]),
    ("/plot/<name>/<type_>/<int:index_>/", "plot", plot, ["GET"]),
]


def init_app(app):
    for rule, endpoint, view_func, methods in routes:
        app.add_url_rule(rule, endpoint, view_func, methods=methods)
