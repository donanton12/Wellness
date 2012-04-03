from django.db import models
from core.models import Record

class TrackingItem(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('auth.User')
    unit = models.CharField(max_length=50)
    daily_cummulative = models.BooleanField(default=False)
    min_value = models.CharField(max_length=5)
    max_value = models.CharField(max_length=5)
    ideal_min_value = models.CharField(max_length=5)
    ideal_max_value = models.CharField(max_length=5)
    reminders = models.ManyToManyField('core.Reminder')

class Medication(models.Model):
    MEDICATION_TYPE=[
        ('otc','OTC'),
        ('prescribed','Prescribed'),
        ('prescribed-otc','PrescribedOTC')
    ]
    WAY_TAKEN = [
        (None, ''),
        ('by-mouth', 'By mouth'),
        ('in-right-ear', 'In Right ear'),
        ('in-both-ears', 'In Both ears'),
        ('in-left-ear', 'In Left ear'),
        ('in-right-eye', 'In Right eye'),
        ('in-both-eyes', 'In Both eyes'),
        ('in-left-eye', 'In Left eye'),
        ('in-nose', 'In Nose'),
        ('inhalation', 'Inhalation'),
        ('intravenous', 'Intravenous'),
        ('topical', 'Topical'),
        ('rectal', 'Rectal'),
        ('vaginal', 'Vaginal'),
        ('under-tongue', 'Under tongue'),
        ('subcataneous', 'Subcataneous'),
    ]
    STRENGTH_UNIT = [
        (None, ''),
        ('gram', 'Gram (g)'),
        ('milligram', 'Milligram (mg)'),
        ('microgram', 'Microgram (mcg)'),
        ('percent', 'Percent (%)'),
    ]
    
    medication_type = models.CharField(max_length=10, choices=MEDICATION_TYPE)
    way_taken = models.CharField(max_length=10, choices=WAY_TAKEN)
    
    strength = models.CharField(max_length=50)
    strength_unit = models.CharField(max_length=50, choices=STRENGTH_UNIT)
    side_effects = models.CharField(max_length=200)
    
class Prescription(Record):
    UNIT = [
        (None, ''),
        ('tablet', 'Tablet(s)'),         
        ('capsule', 'Capsule(s)'),
        ('lozenge', 'Lozenge(s)'),
        ('drop', 'Drop(s)'),
        ('suppository', 'Suppository'),
        ('ointment', 'Ointment'),
        ('millilitre', 'Millilitre (mL)'),
        ('teaspoon', 'Teaspoon(Tbsp)'),
        ('ounce', 'Ounce(oz)'),
    ]
    PERIODS = [
        ('as-needed', 'As needed'),
        ('per-hour', 'Per hour'),
        ('per-day', 'Per day'),
        ('per-week', 'Per week'),
        ('per-month', 'Per month'),
        ('per-year', 'Per year')
    ]
    date_started = models.DateField()
    date_ended = models.DateField()
    date_prescribed = models.DateField()
    reason = models.CharField(max_length=300)
    quantity = models.SmallIntegerField()
    unit = models.CharField(max_length=50, choices=UNIT)
    frequency = models.CharField(max_length=50, choices=[(n, '%s time%s' % (n, 's' if n > 1 else '')) for n in range(1,12)])
    period = models.CharField(max_length=50, choices=PERIODS)
    prescribed_by = models.ForeignKey('healthprovider.HealthWorker')

