from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imageupload.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^file/', include('file.urls')),
    url(r'^user/', include('people.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
