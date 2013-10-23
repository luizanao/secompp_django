
## Dependencias django
from django.conf.urls import patterns, include, url
from django.views.defaults import *
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app_principal.views.home', name='index'),

<<<<<<< HEAD
    #(r'^avisos/$', 'app_principal.views.aviso'),
    #(r'^avisos/(?P<slug>.*)/$', 'app_principal.views.aviso_slug'),
    

    
=======
    url(r'^contato/', 'app_principal.views.contato', name='contato'),
    url(r'^obrigado/', 'app_principal.views.obrigado', name='obrigado'),

>>>>>>> d244d51c5a7c9edf872a8425deb08d90868cc7de
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
