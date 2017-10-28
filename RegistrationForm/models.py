"""from django.db import models

# Create your models here.
from django.db import models
from django.forms import ModelForm

CHOICES = (
    ('DeskJob', 'Desk Job'),
    ('FieldJob', 'Field Job'),

)
class User(models.Model):
    name = models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    job = models.CharField(max_length=100, choices=CHOICES)


    def __str__(self):              # __unicode__ on Python 2
        return self.name
    """

from django.db import models

# Create your models here.
from django.db import models
from django.forms import ModelForm

CHOICES = (
    ('DeskJob_comp', 'DeskJob_comp'),
    ('DeskJob_normal', 'DeskJob_normal'),

)

CHOICES2 = (
    ('DayJob','DayJob'),
    ('NightJob','NightJob'),
)

class User(models.Model):
    name = models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    job = models.CharField(max_length=100, choices=CHOICES)
    job_time = models.CharField(max_length=100, choices=CHOICES2)
    twitter_handle= models.CharField(max_length=20)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

