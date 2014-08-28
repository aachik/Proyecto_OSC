from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',

  url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)


urlpatterns = patterns('app.views',

    (r'^admin/', include(admin.site.urls)),
    (r"^organizacion/(?P<pk>\d+)/$", "organizacion"),
    (r"^form/","form"),
    (r"^admin/", "admin"),
    (r"","main"),


)

if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)