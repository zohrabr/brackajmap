from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^crime/',include('crime.urls')),
        url(r'^accounts', include('allauth.urls')),
        url(r'^admin/', include(admin.site.urls)),
)
