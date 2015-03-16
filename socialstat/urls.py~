from django.conf.urls import patterns, include, url
from retrieveimage.views import hello_world
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socialstat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/1234/preview',hello_world),
)
