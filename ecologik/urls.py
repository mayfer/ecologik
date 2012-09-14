from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecologik.views.home', name='home'),
    # url(r'^ecologik/', include('ecologik.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'ecologik.views.index', name='index'),
	url(r'^services/?$', 'ecologik.views.services', name='services'),
	url(r'^about/?$', 'ecologik.views.about', name='about'),
	url(r'^contact/?$', 'ecologik.views.contact', name='contact'),

	url(r'^plants/?$', 'ecologik.views.plants', name='plants'),
	url(r'^plants/(crops|herbs|shrubs|trees)/?$', 'ecologik.views.plants', name='plants-section'),
)
