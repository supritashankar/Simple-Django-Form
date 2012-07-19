from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite3.views.home', name='home'),
    # url(r'^mysite3/', include('mysite3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^search/$','books.views.search'),
    url(r'^add_publisher/$', 'books.views.add_publisher'),
    url(r'^add_publisher/thanks/$','books.views.thanks'),
    url(r'^admin/', include(admin.site.urls)),
)
