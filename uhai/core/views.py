from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from uhai.core.models import Relationship

def model_view(request, pk=None, 
         template_name='',
         queryset=None,
         model_form_class=None,
         model_form_classes=[],
         action='view',
         data = {},
         initial_form_data=lambda:{},
         save_form=lambda form:form.save(),
         redirect_to=None,
         extra_action=lambda request, action:None,
         context_object_name=lambda model_obj:model_obj._meta.object_name.lower(),
         context_object_name_plural=lambda model_obj:model_obj._meta.object_name.lower()+'s',
         context_form_name='form',
         extra_data={}):
	
	success = False
	if action in ('view','edit','delete', 'create'):
		try:
			model_obj = queryset.filter(pk=pk).get() if pk else queryset.model()
		except queryset.model.DoesNotExist:
			raise Http404()
		data[context_object_name(model_obj)] = model_obj
	else:
		data[context_object_name_plural(queryset.model)] = queryset

	if not template_name:
		template_name = "%s/%s_%s.html" % (queryset.model._meta.app_label, queryset.model._meta.object_name.lower(), action)
		
	if request.method == 'GET':
		if action in ['create', 'view', 'edit', 'delete', 'list']:
			if action in ['create', 'edit', 'delete']:
				initial = initial_form_data()                
				data[context_form_name] = model_form_class() if initial else model_form_class(initial=initial)
		else:
			extra_action(request, action)
		
	elif request.method == 'POST':
		if action == 'edit' or action == 'create':
			if not model_form_classes and model_form_class:
				model_form_classes.append(model_form_class)
				
			for model_form_class in model_form_classes:  
				form = model_form_class(request.POST, request.FILES, instance=model_obj)
				if form.is_valid():
					o = save_form(form)
					redirect_to = ['%s-detail' % queryset.model.__name__.lower(), o.pk]
					success = True
					
			if success:
				return HttpResponseRedirect(reverse(**redirect_to))
			data[context_form_name] = form
		elif action == 'delete':
			if model_obj:
				model_obj.delete()
		else:
			extra_action(request, action)
			
	data.update(extra_data)
	return render_to_response(template_name, data, context_instance=RequestContext(request))

@login_required
def relationship(request, *args, **kwargs):
    queryset = Relationship.objects.filter(person_a=request.user.profile)
    return model_view(request, queryset=queryset, *args, **kwargs)

relationshiptype = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))