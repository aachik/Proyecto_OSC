from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',

  url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)


urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    (r"^organizacion/(?P<pk>\d+)/$", "app.views.organizacion"),
    (r"^form/","app.views.formulario"),
    (r"^admin/", "app.views.admin"),
    (r"^contacto/", "app.views.contacto"),
    (r'^search/$', 'app.views.search'),
    (r'^blog/','blog.views.post_list'),
    (r"^$","app.views.main"),


)







if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)