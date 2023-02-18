from django.db import models
from django.contrib.auth import get_user_model

# from jsonfield import JSONField
# from django.contrib.postgres.fields import JSONField

user = get_user_model()
# Create your models here.
class eventType(models.Model):
    Name        =models.CharField(max_length=50, unique=True, blank=True)
    Description =models.CharField(max_length=50, blank=True)
    CreatedDate =models.DateField(auto_now_add=True)
    is_active   =models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name

class eventName(models.Model):
    Typeid      =models.ForeignKey(eventType, on_delete=models.CASCADE)
    Name        =models.CharField(max_length=50, unique=True, blank=True)
    Description =models.CharField(max_length=50, blank=True)
    CreatedDate =models.DateField(auto_now_add=True)
    is_active   =models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name

class userProfile(models.Model):
    user            =models.ForeignKey(user, on_delete=models.CASCADE)
    id_user         =models.IntegerField()
    userFirstName   =models.CharField(max_length=50, blank=True)
    userLastName    =models.CharField(max_length=50, blank=True)
    userMiddleName  =models.CharField(max_length=50, blank=True)
    userGender      =models.CharField(max_length=50, blank=True) 
    userDOB         =models.CharField(max_length=50, blank=True)
    userPhone       =models.CharField(max_length=10, blank=True)
    userAddress     =models.CharField(max_length=50, blank=True)
    userDistrict    =models.CharField(max_length=50, blank=True)
    userState       =models.CharField(max_length=50, blank=True)
    userPinCode     =models.CharField(max_length=6, blank=True)
    userRepState    =models.CharField(max_length=50, blank=True)
    userAadhar      =models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

class userPerfData(models.Model):
    user        =models.ForeignKey(user, on_delete=models.CASCADE)
    eventID     =models.ForeignKey(eventName, on_delete=models.CASCADE)
    attempt     =models.IntegerField()
    fld_value   =models.TextField()
    event_date  =models.DateTimeField()
    CreatedDate =models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user