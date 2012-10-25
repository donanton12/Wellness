from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

#apps
urlpatterns = patterns('',
	#app level
	url(r'^$', 'uhai.views.index', name="index"),	
	url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^about/$', TemplateView.as_view(template_name='website/how_it_works.html'), name="about"),
    url(r'^terms-of-service/$', TemplateView.as_view(template_name='website/terms-conditions.html'), name="terms_and_conditions"),
    url(r'^privacy-policy/$', TemplateView.as_view(template_name='website/privacy_policy.html'), name="privacy-policy"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT, 'show_indexes': True}),
    )
