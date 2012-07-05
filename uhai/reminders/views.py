from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from django.shortcuts import render_to_response

from uhai.core.views import model_view

@login_required
def calendar(request, template_name="reminders/calendar.html"):	
	from uhai.records.forms import EncounterForm
	return render_to_response(template_name, {'form':EncounterForm()}, context_instance=RequestContext(request))
	
event = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
