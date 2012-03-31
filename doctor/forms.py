from django.forms import form
from models import *

class DoctorAdminForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.charField()
	email = forms.EmailField()
	
	class Meta:
		model = Doctor
		sequence = ['first_name', 'middle_name', 'last_name', 'email']
		exclude = ['user']

class DoctorForm(DoctorAdminForm):
	class Meta:
		model = Doctor
		sequence = ['first_name', 'middle_name', 'last_name', 'email']
		exclude = ['user']


