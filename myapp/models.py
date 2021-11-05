from django.db import models
from django.db import models
from django.db.models.fields import DateField

#from myApp.views import contact

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.desc + ' by ' + self.name

class Feedback(models.Model):
   
    feedback=models.TextField()
    def __str__(self):
        return self.feedback
# Create your models here.
