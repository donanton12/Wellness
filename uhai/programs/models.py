from django.db import models
from uhai.core.models import *
	
class Program(OwnerModel):
    '''
    This represents either an Employee Assistance Program (EAP)
    or a Patient Assistance Program (PAP). An example is a program
    to help Alcoholics.
    '''
    name = models.CharField(max_length=100)
    problem = models.ForeignKey("records.Problem")
    is_public = models.BooleanField(default=False, editable=False, help_text='Can be used by other Patients, Users as a Template. Leave unchecked, to be private')
    concept_notes = models.TextField(null=True, blank=True)
    expected_outcome_notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
    	return str(self.name)

    class Meta:
        permissions = ( 
            ('view_program', 'View program'), 
        )

class EnrolledProgram(models.Model):
    '''
    Patient/Employee can be enrolled in a Program to help them
    Anyone can be enrolled to this... Even Doctors or even employees
    of Insurance companies
	Even Patients can enroll themselves to a program, for example,
	Weight loss program...
    '''
    program = models.ForeignKey("Program")
    enrollee = models.ForeignKey("patients.Patient", related_name='enrollee')
    enroller = models.ForeignKey("auth.User", related_name='enroller', verbose_name="Enrolled By")
    date_enrolled = models.DateField(auto_now=True)
    date_completed = models.DateField()
    outcome_notes = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return 'Program enrolled to: %s by %s' % (self.program, self.enrollee)
    
    class Meta:
        permissions = ( 
            ('view_enrolledprogram', 'View enrolled program'), 
        )

class ProgramWorkflow(models.Model):
    '''
    A program may involve certain steps that define progress
    in the program; thus we have the path and the nodes.
    The nodes are represented by the @see: ProgramWorkflowState
    and the Path represented by @see: ProgramWorkflow
    Example: An Alcoholic Program would have Workflows like:
    Family Intervention, Withdrawal...    
    '''
    name = models.CharField(max_length=100)
    program = models.ForeignKey("Program")
    concept_notes = models.TextField()
    continued = models.BooleanField(default=True)
    days = models.IntegerField(default=0, blank=True, null=True)
    
    def __unicode__(self):
    	return self.name
    
    class Meta:
        permissions = ( 
            ('view_enrolledprogram', 'View enrolled program'), 
        )
    
class ProgramWorkflowState(models.Model):
    '''
    This represents a node/milestone state of @see: PrenrolleeogramWorkflow
    in the program.
    A state in the Alcoholic Program would be: Starting, Completed, or something
    '''
    name = models.CharField(max_length=120)
    program_workflow = models.ForeignKey("ProgramWorkflow")
    weight = models.IntegerField(default=0)
    initial = models.BooleanField(default=False)
    terminal = models.BooleanField(default=False)
    concept_notes = models.TextField()
    
    def __unicode__(self):
    	return 'Node: %s %s' % (self.name, self.program_workflow)
    
    class Meta:
        permissions = ( 
            ('view_programworkflowstate', 'View program workflow state'), 
        )
