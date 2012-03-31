from django.db import models
from django.contrib.auth.models import User
from fields import  *

# Create your models here.
class Person(models.Model):
	TITLES = (
		('mr','Mr.'),
		('mrs','Mrs.'),
		('miss','Miss'),
		('dr', 'Dr.'),
		('prof', 'Professor'),
	)

	title = models.CharField(max_length=20, choices=TITLES)
	middle_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)

	postal_address = models.CharField(max_length=50)
	photo = models.ImageField(upload_to='photos')
	gender = models.CharField(max_length=20, choices=(('male', 'Male'),('female', 'Female')))

	country = CountryField()
	nationality = models.CharField(max_length=150, default='kenyan')

	user = models.ForeignKey(User, unique=True)
	
	date_edited = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True
	
User.profile = lambda self:self.__class__.objects.get_or_create(user=self.user)[0]

