from django.conf.urls.defaults import * 

urlpatterns = patterns('',
    url(r'^login/?$', 'uhai.userprofile.views.login', {
    		'template_name':'userprofile/login.html'
    	}, name='login'
    ),
    url(r'^logout/?$','uhai.userprofile.views.logout', {
    		'redirect_field_name':'next',
    		'template_name':'userprofile/logout.html'
    	}, name='logout'
    ),
)