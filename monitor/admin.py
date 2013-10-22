from django.contrib import admin
from monitor.models import Line, IntValue, FloatValue, Statistic, StrValue

admin.site.register(Line)
admin.site.register(IntValue)
admin.site.register(FloatValue)
admin.site.register(Statistic)
admin.site.register(StrValue)
