from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

#django
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

#apps
urlpatterns += patterns('',
	#app level
	url(r'^$', 'uhai.views.index', name="index"),
	url(r'^home/$', 'uhai.views.dashboard', name="home"),
	url(r'^start/use-as/$', 'uhai.views.use_as', name="choose-use-as"),
	url(r'^use-as/(?P<type>patient|insurance-agent|health-worker|site-admin|employer)/$', 'uhai.views.use_as', name="use-as"),
	url(r'^admin_tools/', include('admin_tools.urls')),
	url(r'^stats/', include('uhai.stats.urls')),
	url(r'^records/', include('uhai.records.urls')),
	url(r'^providers/', include('uhai.providers.urls')),
	url(r'^insurance/', include('uhai.insurance.urls')),
	url(r'^account/sharer/', include('uhai.sharer.urls')),	
	url(r'^records/', include('uhai.patients.urls')),
	url(r'^reminders/', include('uhai.reminders.urls')),
	url(r'^programs/', include('uhai.programs.urls')),
	url(r'^medication/', include('uhai.medication.urls')),
	
	url(r'^search/', include('uhai.search.urls')),
	url(r'^sms/', include('uhai.sms.urls')),
	
	url(r'', include('uhai.core.urls')),
	url(r'', include('uhai.userprofile.urls')),
	
	#view level
    url(r'^login/$', 'uhai.userprofile.views.login', {'template_name':'userprofile/login.html'}, name='login'),
    url(r'^logout/$','uhai.userprofile.views.logout', {'redirect_field_name':'next','template_name':'userprofile/logout.html'}, name='logout'),
)

urlpatterns += patterns('',
    url(r'^about/$', TemplateView.as_view(template_name='website/how_it_works.html'), name="about"),
    url(r'^terms-of-service/$', TemplateView.as_view(template_name='website/terms-conditions.html'), name="terms_and_conditions"),
    url(r'^privacy-policy/$', TemplateView.as_view(template_name='website/privacy_policy.html'), name="privacy-policy"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT, 'show_indexes': True}),
    )
