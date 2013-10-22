from django.db import models


class Statistic(models.Model):
    name = models.CharField(unique=True, max_length=40)

    def __unicode__(self):
        return "<statistic %s>" % self.name


class Line(models.Model):
    statistic = models.ForeignKey(Statistic, related_name='lines')
    moment = models.DateTimeField()

    class Meta:
        unique_together = ('statistic', 'moment')

    def __unicode__(self):
        return "<line %s %s>" % (self.statistic, self.moment)


class Value(models.Model):
    index = models.IntegerField()

    def __unicode__(self):
        return "<%s %s %s %s>" % (self.__class__, self.line, self.index,
                                  self.value)

    class Meta:
        abstract = True


class IntValue(Value):
    line = models.ForeignKey(Line, related_name='int_values')
    value = models.IntegerField()


class FloatValue(Value):
    line = models.ForeignKey(Line, related_name='float_values')
    value = models.FloatField()


class StrValue(Value):
    line = models.ForeignKey(Line, related_name='str_values')
    value = models.CharField(max_length=40)
