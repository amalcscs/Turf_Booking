from xmlrpc.client import boolean
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class designation(models.Model):
    designation = models.CharField(max_length=100)
    files=models.FileField(upload_to = 'images/', null=True, blank=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.designation

class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='userregistrationdesignation', null=True, blank=True)
    Firstname = models.CharField(max_length=240, null=True)
    Lastname = models.CharField(max_length=240, null=True)
    place = models.CharField(max_length=240, null=True)
    address = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.Firstname


class Turf(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                             related_name='turfuser', null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='turfdesignation', null=True, blank=True)
    Turfname = models.CharField(max_length=240, null=True)
    location = models.CharField(max_length=240, null=True)
    sport = models.CharField(max_length=240, null=True)
    
    capacity = models.CharField(max_length=240, null=True)
    Price = models.CharField(max_length=240, null=True)
    amenties = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.Turfname


class Teams(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                             related_name='Teamsuser', null=True, blank=True)
    teamname = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.teamname

class Matches(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                             related_name='Matchesuser', null=True, blank=True)
    turf = models.ForeignKey(Turf, on_delete=models.DO_NOTHING,
                             related_name='matchturf', null=True, blank=True)
    location = models.ForeignKey(Turf, on_delete=models.DO_NOTHING,
                             related_name='matchlocation', null=True, blank=True)
    firstteam = models.CharField(max_length=240, null=True)
    secondteam = models.CharField(max_length=240, null=True)
    result = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.firstteam


class match_result(models.Model):
    turf = models.ForeignKey(Turf, on_delete=models.DO_NOTHING,
                             related_name='match_resultturf', null=True, blank=True)
    location = models.ForeignKey(Turf, on_delete=models.DO_NOTHING,
                             related_name='match_resultlocation', null=True, blank=True)
    firstteam = models.ForeignKey(Turf, on_delete=models.DO_NOTHING,
                             related_name='match_resultfirstteam', null=True, blank=True)
    secondteam = models.ForeignKey(Turf, on_delete=models.DO_NOTHING,
                             related_name='match_resultsecondteam', null=True, blank=True)
    win_team = models.ForeignKey(Turf, on_delete=models.DO_NOTHING,
                             related_name='match_resultwin_team', null=True, blank=True)
    loss_team = models.ForeignKey(Turf, on_delete=models.DO_NOTHING,
                             related_name='match_resultloss_team', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    match_status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.match_status


class Contact_messages(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                             related_name='Contact_messagesuser', null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='Contact_messagesdesignation', null=True, blank=True)
    name = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    message_type = models.CharField(max_length=240, null=True)
    message = models.CharField(max_length=240, null=True)
    

    def __str__(self):
        return self.name