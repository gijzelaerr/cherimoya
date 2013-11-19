from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        return instance


class Statistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)

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


class ComplexValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.Integer, db.ForeignKey(Line.id))
    line = db.relationship("Line", backref=db.backref('complex_values'))
    real = db.Column(db.Float)
    imag = db.Column(db.Float)
    index = db.Column(db.Integer)

    def __init__(self, value, index, line):
        self.real = value.real
        self.imag = value.imag
        self.index = index
        self.line = line

    @property
    def value(self):
        return complex(self.real, self.imag)

    def __repr__(self):
        return "<%s %s %s %s>" % (self.__class__, self.line, self.index,
                                  self.value)