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
    designation = models.ForeignKey(designation, on_delete=models.CASCADE,
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
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='turfuser', null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.CASCADE,
                                    related_name='turfdesignation', null=True, blank=True)
    Turfname = models.CharField(max_length=240, null=True)
    location = models.CharField(max_length=240, null=True)
    locationurl = models.CharField(max_length=240, null=True)
    sport = models.CharField(max_length=240, null=True)
    
    capacity = models.CharField(max_length=240, null=True)
    Price = models.CharField(max_length=240, null=True)
    Playrate = models.CharField(max_length=240, null=True)
    amenties = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='0')

    def __str__(self):
        return self.Turfname


class Teams(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='Teamsuser', null=True, blank=True)
    teamname = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.teamname

class Matches(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='Matchesuser', null=True, blank=True)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE,
                             related_name='matchturf', null=True, blank=True)
    
    matchname = models.CharField(max_length=240, null=True)
    firstteam = models.CharField(max_length=240, null=True)
    secondteam = models.CharField(max_length=240, null=True)
    result = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    fromtime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')
    Ticketprice = models.CharField(max_length=240, null=True)
    quantity = models.CharField(max_length=240, null=True)
    total = models.CharField(max_length=240, null=True)
    paymentstatus = models.CharField(max_length=240, null=True, default='0')
    paymentdate = models.DateField(null=True, blank=True)
    bankname = models.CharField(max_length=240, null=True)
    accountnumber = models.CharField(max_length=240, null=True)
    ifsccode = models.CharField(max_length=240, null=True)
    branchname = models.CharField(max_length=240, null=True)
    amount = models.CharField(max_length=240, null=True)
    turfuser_id = models.CharField(max_length=240, null=True)
    
    

    def __str__(self):
        return self.firstteam


class Matchresult(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='match_resultuser', null=True, blank=True)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE,
                             related_name='match_resultturf', null=True, blank=True)
    firstteam = models.ForeignKey(Teams, on_delete=models.CASCADE,
                             related_name='match_resultfirstteam', null=True, blank=True)
    secondteam = models.ForeignKey(Teams, on_delete=models.CASCADE,
                             related_name='match_resultsecondteam', null=True, blank=True)
    win_team = models.ForeignKey(Teams, on_delete=models.CASCADE,
                             related_name='match_resultwin_team', null=True, blank=True)
    loss_team = models.ForeignKey(Teams, on_delete=models.CASCADE,
                             related_name='match_resultloss_team', null=True, blank=True)
    matchname = models.ForeignKey(Matches, on_delete=models.CASCADE,
                             related_name='match_resultmatchname', null=True, blank=True,default='')
    date = models.DateField(null=True, blank=True)
    fromtime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    match_status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.match_status


class Contact_messages(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='Contact_messagesuser', null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.CASCADE,
                                    related_name='Contact_messagesdesignation', null=True, blank=True)
    name = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    message_type = models.CharField(max_length=240, null=True)
    message = models.CharField(max_length=240, null=True)
    reply = models.CharField(max_length=240, null=True)
    repliedby = models.CharField(max_length=240, null=True)
    replyto = models.CharField(max_length=240, null=True)
    

    def __str__(self):
        return self.name


class TurfBooking(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='TurfBookinguser', null=True, blank=True)
    owner = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='TurfBookingowner', null=True, blank=True)
    Turf = models.ForeignKey(Turf, on_delete=models.CASCADE,
                                    related_name='TurfBookingTurf', null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.CASCADE,
                                    related_name='TurfBookingdesignation', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    fromtime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    sport = models.CharField(max_length=240, null=True)
    gamestructure = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='0')
    
    def __str__(self):
        return self.sport


class Payment(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='Paymentuser', null=True, blank=True)
    matches = models.ForeignKey(Matches, on_delete=models.CASCADE,
                             related_name='Paymentmatches', null=True, blank=True)
    Turf = models.ForeignKey(Turf, on_delete=models.CASCADE,
                                    related_name='PaymentTurf', null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.CASCADE,
                                    related_name='Paymentdesignation', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    bankname = models.CharField(max_length=240, null=True)
    accountnumber = models.CharField(max_length=240, null=True)
    ifsccode = models.CharField(max_length=240, null=True)
    branchname = models.CharField(max_length=240, null=True)
    amount = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='0')
    
    def __str__(self):
        return self.bankname


class Shopcategory(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='Shopcategoryuser', null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.CASCADE,
                             related_name='Shopcategorydesignation', null=True, blank=True)
    category = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='0')
    
    def __str__(self):
        return self.category


class Shopitems(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='Shopitemsuser', null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.CASCADE,
                             related_name='Shopitemsdesignation', null=True, blank=True)
    category = models.CharField(max_length=240, null=True)
    companyname = models.CharField(max_length=240, null=True)
    itemname = models.CharField(max_length=240, null=True)
    price = models.CharField(max_length=240, null=True)
    size = models.CharField(max_length=240, null=True)
    color = models.CharField(max_length=240, null=True)
    quantity = models.CharField(max_length=240, null=True)
    finalprice = models.CharField(max_length=240, null=True)
    subtotal = models.CharField(max_length=240, null=True)
    tax = models.CharField(max_length=240, null=True)
    total = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    description = models.CharField(max_length=240, null=True)
    deliverydate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='0')
    
    def __str__(self):
        return self.category

class AddShopitems(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='AddShopitemssuser', null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.CASCADE,
                             related_name='AddShopitemsdesignation', null=True, blank=True)
    category = models.ForeignKey(Shopcategory, on_delete=models.CASCADE,
                             related_name='AddShopitemsuser', null=True, blank=True)
    companyname = models.CharField(max_length=240, null=True)
    itemname = models.CharField(max_length=240, null=True)
    price = models.CharField(max_length=240, null=True)
    size = models.CharField(max_length=240, null=True)
    color = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    description = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='0')
    
    def __str__(self):
        return self.companyname


class Shoppayment(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE,
                             related_name='Shoppaymentuser', null=True, blank=True)
    Shopitems = models.ForeignKey(Shopitems, on_delete=models.CASCADE,
                             related_name='Shoppaymentuser', null=True, blank=True)
    items = models.CharField(max_length=240, null=True)
    subtotal = models.CharField(max_length=240, null=True)
    tax = models.CharField(max_length=240, null=True)
    total = models.CharField(max_length=240, null=True)
    date = models.DateField(null=True, blank=True)
    bankname = models.CharField(max_length=240, null=True)
    accountnumber = models.CharField(max_length=240, null=True)
    ifsccode = models.CharField(max_length=240, null=True)
    branchname = models.CharField(max_length=240, null=True)
    amount = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='0')
    
    def __str__(self):
        return self.subtotal