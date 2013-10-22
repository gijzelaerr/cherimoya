from django.db import models


class Statistic(models.Model):
    name = models.CharField(unique=True, max_length=40)


class Line(models.Model):
    statistic = models.ForeignKey(Statistic, related_name='lines')
    moment = models.DateTimeField()


class IntValue(models.Model):
    statistic = models.ForeignKey(Line, related_name='int_values')
    index = models.IntegerField()
    value = models.IntegerField()


class FloatValue(models.Model):
    statistic = models.ForeignKey(Line, related_name='float_values')
    index = models.IntegerField()
    value = models.FloatField()


class StrValue(models.Model):
    statistic = models.ForeignKey(Line, related_name='str_values')
    index = models.IntegerField()
    value = models.CharField(max_length=40)