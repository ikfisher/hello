from django.conf.urls import patterns, include, url

from django.contrib import admin
from hello.views import hello
from hello.views import current_datetime
from hello.views import next_time
from hello.views import temp

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^now/$', current_datetime),
    url(r'^now/next/(\d{1,2})/$', next_time),
    url(r'^now/name/$', temp),
)
