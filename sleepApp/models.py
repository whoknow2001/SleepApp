from djongo import models
from django import forms

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.
class Notification(models.Model):
    Time = models.DateTimeField()
    Text = models.TextField(max_length=1000)
    class Meta:
        abstract = True

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('Time','Text')

class User(models.Model):
    Id = models.TextField(primary_key=True,max_length=100)
    Name = models.TextField(max_length=500,null=False,blank=False)
    Cmnd = models.TextField(max_length=20,null=True)
    Email = models.TextField(max_length=100,null=True)
    Phone = models.TextField(max_length=20,null=True)
    Avatar = models.ImageField(upload_to = upload_to,blank = True,null = True)
    Notification = models.ArrayField(
        model_container= Notification,
        model_form_class=NotificationForm
    )
    objects = models.DjongoManager()

class Account(models.Model):
    Id = models.TextField(primary_key=True,max_length=100)
    Username = models.TextField(max_length=500,null=False,blank=False)
    Password = models.TextField(max_length=500,null=False,blank=False)
    Role = models.TextField(max_length=500,null=False,blank=False)
    objects = models.DjongoManager()
