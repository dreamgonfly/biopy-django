from django.conf.urls import patterns, include, url
from django.contrib import admin
from student.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sandbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/$', student_view),
    url(r'^api/(?P<msg>\w+)$', json),
)
