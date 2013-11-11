from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Statistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<statistic %s>" % self.name


class Line(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    statistic_id = db.Column(db.Integer, db.ForeignKey(Statistic.id))
    statistic = db.relationship(Statistic, backref=db.backref('lines'))
    moment = db.Column(db.DateTime)

    __table_args__ = (db.UniqueConstraint('statistic_id', 'moment'),)

    def __repr__(self):
        return "<line %s %s>" % (self.statistic, self.moment)


class IntValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.Integer, db.ForeignKey(Line.id))
    line = db.relationship("Line", backref=db.backref('int_values'))
    value = db.Column(db.Integer)
    index = db.Column(db.Integer)

    def __repr__(self):
        return "<%s %s %s %s>" % (self.__class__, self.line, self.index,
                                  self.value)


class FloatValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.Integer, db.ForeignKey(Line.id))
    line = db.relationship("Line", backref=db.backref('float_values'))
    value = db.Column(db.Float)
    index = db.Column(db.Integer)

    def __repr__(self):
        return "<%s %s %s %s>" % (self.__class__, self.line, self.index,
                                  self.value)


class StrValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.Integer, db.ForeignKey(Line.id))
    line = db.relationship("Line", backref=db.backref('str_values'))
    value = db.Column(db.String(40))
    index = db.Column(db.Integer)

    def __repr__(self):
        return "<%s %s %s %s>" % (self.__class__, self.line, self.index,
                                  self.value)