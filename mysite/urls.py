from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from books.views import search,contact
from mysite.views import current_time
from mysite.views import hours_more
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

     url(r'^time/$',current_time),
    url(r'^ahead_time/$',hours_more,{'offset':7}),
    #we can also use the below pattern
    #url(r'^ahead_time/([0-9])/$',hours_more),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^search/$', search),
    url(r'^contact/$',contact),
)
