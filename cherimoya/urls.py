from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cherimoya.views.home', name='home'),
    # url(r'^cherimoya/', include('cherimoya.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
