import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from django. contrib import messages
from django.conf import settings
from.models import *
from datetime import datetime,date,timedelta
from django.http import HttpResponse, HttpResponseRedirect

#Login

def log(request):
    owner = designation.objects.get(designation="owner")
    users = designation.objects.get(designation="users")
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'Admin_index')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=owner.id).exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['O_id'] = member.designation_id
                request.session['O_id'] = member.id 
                mem=user_registration.objects.filter(id= member.id)
                
                return render(request,'index.html',{'mem':mem})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=users.id).exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['U_id'] = member.designation_id
                request.session['U_id'] = member.id 
                mem1=user_registration.objects.filter(id= member.id)
                
                return render(request,'User_index.html',{'mem1':mem1})
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
    return render(request,'login.html')

#Registration

def regis(request):
    
    if request.method == 'POST':
        des=designation.objects.get(designation="users")
        acc = user_registration()
        acc.fullname = request.POST['firstname']
        acc.Lastname = request.POST['lastname']
        acc.mobile = request.POST['mobile']
        acc.place = request.POST['place']
        acc.address = request.POST['address']
        acc.pincode = request.POST['pincode']
        acc.email = request.POST['email']
        acc.password = request.POST['conpassword']
        acc.photo = request.FILES['profile_pic']
        acc.designation_id = des.id
        acc.save()
        msg_success = "Registration successfull"
        return render(request, 'reg.html', {'msg_success': msg_success})
    return render(request, 'reg.html') 

#*******Admin module*******

#Admin Logout

def Admin_logout(request):
    if 'SAdm_id' in request.session:  
        request.session.flush()
        return redirect("/")
    else:
        return redirect('/') 

#Admin Index

def Admin_index(request):
        owner = designation.objects.get(designation='owner')
        ownercount=Contact_messages.objects.filter(designation_id=owner).count()
        return render(request, 'Admin_index.html',{'ownercount':ownercount})

def Admin_Turf_requests(request):
    desig = designation.objects.get(designation="owner")
    req1 = Turf.objects.filter(designation_id=desig)
    return render(request, 'Admin_Turf_requests.html',{'req1':req1})

def Admin_notification(request):
    
        desig = designation.objects.get(designation="owner")
        mess1 = Contact_messages.objects.filter(designation_id=desig)
        return render(request, 'Admin_notification.html',{'mess1':mess1})

def AdminTurfapprove(request,id):
    
    n = Turf.objects.filter(id=id).update(status ="approved")
    return redirect('Admin_Turf_requests')

def AdminTurfrejected(request,id):
    
    n = Turf.objects.filter(id=id).update(status ="rejected")
    return redirect('Admin_Turf_requests')

def Admin_messagereply(request,id):
    if request.method == 'POST':
        v = Contact_messages.objects.get(id=id)
        v.reply=request.POST.get('reply')
        v.save()
    return redirect('Admin_notification')

def Admin_view_matches(request):
    turf1 = Turf.objects.all()
    view = Matchresult.objects.all().order_by("-id")
    return render(request, 'Admin_view_matches.html',{'view':view,'turf1':turf1})

def Admin_contact(request):
      return render(request, 'Admin_contact.html')


def about(request):
  return render(request, 'aboutus.html')

def matches(request):
  return render(request, 'matches.html')

def shop(request):
  return render(request, 'shoplist.html')

def turf(request):
  return render(request, 'turfs.html')

def cart(request):
  return render(request, 'cart.html')

def books(request):
  return render(request, 'bookings.html') 


  
def book_ticket(request):
  return render(request, 'book_ticket.html')

def buy_tickets_readmore(request):
  return render(request, 'buy_tickets_readmore.html') 
  
def payment(request):
  return render(request, 'payment.html') 



def sign(request):
  return render(request, 'signup.html') 

#****Owner module******

#index

def indexo(request):
    if 'O_id' in request.session:
        if request.session.has_key('O_id'):
            O_id = request.session['O_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=O_id)
        users = designation.objects.get(designation='users')
        Act_count=Contact_messages.objects.filter(designation_id=users).count()
        return render(request, 'index.html',{'mem':mem,'Act_count':Act_count})

#Owner logout

def Owner_logout(request):
    if 'O_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

#Turf Adding

def add(request):
    if 'O_id' in request.session:
        if request.session.has_key('O_id'):
            O_id = request.session['O_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=O_id)
        if request.method == 'POST':
            abc = Turf()
            abc.Turfname = request.POST['Turfname']
            abc.location = request.POST['Location']
            abc.locationurl = request.POST['loc_url']
            abc.sport = request.POST['Sport']
            abc.capacity = request.POST['Capacity']
            abc.Price = request.POST['Price']
            abc.amenties = request.POST['Amenties']
            abc.photo = request.FILES['files']
            abc.user_id  = O_id
            abc.save()
            msg_success = "Turf Added successfull"
            return render(request, 'Addturf.html', {'msg_success': msg_success})
        return render(request, 'Addturf.html',{'mem':mem}) 

def req(request):
    if 'O_id' in request.session:
        if request.session.has_key('O_id'):
            O_id = request.session['O_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=O_id)
        reqe = Turf.objects.filter(user_id=O_id)
        return render(request, 'request.html',{'mem':mem,'reqe':reqe}) 

def Owner_notification(request):
    if 'O_id' in request.session:
        if request.session.has_key('O_id'):
            O_id = request.session['O_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=O_id)
        desig = designation.objects.get(designation="users")
        mess = Contact_messages.objects.filter(designation_id=desig)
        return render(request, 'Owner_notification.html',{'mem':mem,'mess':mess}) 

def Owner_messagereply(request,id):
     if 'O_id' in request.session:
        if request.session.has_key('O_id'):
            O_id = request.session['O_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=O_id)
        if request.method == 'POST':
            v = Contact_messages.objects.get(id=id)
            v.reply=request.POST.get('reply')
            v.repliedby=O_id
            v.save()
        return redirect('Owner_notification')
        
def Owner_book_details(request):
    return render(request,'Owner_book_details.html') 

def Add_match(request):
    if 'O_id' in request.session:
        if request.session.has_key('O_id'):
            O_id = request.session['O_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=O_id)
        m = Turf.objects.all()
        c = Teams.objects.all()
        if request.method == 'POST':
            
            ab = Matches()
            ab.turf_id  = request.POST['turfname']
            ab.location_id  = request.POST['location']
            ab.firstteam = request.POST['firstteam']
            ab.secondteam = request.POST['secondteam']
            ab.photo = request.FILES['image']
            ab.date = datetime.now()
            ab.user_id  = O_id
            ab.save()
            msg_success = "Match Added successfull"
            return render(request, 'Add_match.html', {'msg_success': msg_success})
        return render(request,'Add_match.html',{'mem':mem,'m':m,'c':c}) 

def match_result(request):
    if 'O_id' in request.session:
        if request.session.has_key('O_id'):
            O_id = request.session['O_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=O_id)
        m = Turf.objects.all()
        c = Teams.objects.all()
        if request.method == 'POST':
            
            an = Matchresult()
            an.turf_id   = request.POST['turfname']
            an.location_id  = request.POST['location']
            an.firstteam_id  = request.POST['firstteam']
            an.secondteam_id   = request.POST['secondteam']
            an.win_team_id   = request.POST['winteam']
            an.loss_team_id   = request.POST['lossteam']
            an.photo = request.FILES['image']
            an.date = datetime.now()
            an.user_id  = O_id
            an.save()
            msg_success = "Match result Added successfull"
            return render(request, 'match_result.html', {'msg_success': msg_success})
        return render(request,'match_result.html',{'mem':mem,'m':m,'c':c}) 


def addteam(request):
    if 'O_id' in request.session:
        if request.session.has_key('O_id'):
            O_id = request.session['O_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=O_id)
        if request.method == 'POST':
            
            a = Teams()
            a.teamname  = request.POST['name']
            a.photo = request.FILES['image']
            a.user_id  = O_id
            a.save()
            msg_success = "Team Added successfully"
            return render(request, 'Add_match.html', {'msg_success': msg_success})
        return render(request,'addteam.html',{'mem':mem})


def Owner_contact(request):
    if 'O_id' in request.session:
        if request.session.has_key('O_id'):
            O_id = request.session['O_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=O_id)
        turf=Turf.objects.filter(user_id=O_id)
        des2=designation.objects.get(designation="owner")
        if request.method == 'POST':
            
            a = Contact_messages()
            a.name  = request.POST['name']
            a.email  = request.POST['email']
            a.message_type  = request.POST['messagetype']
            a.message  = request.POST['message']
            a.user_id  = O_id
            a.designation_id = des2.id
            a.save()
            msg_success = "Message send successfully"
            return render(request, 'owner_contactus.html', {'msg_success': msg_success})
        return render(request, 'owner_contactus.html',{'mem':mem,'turf':turf})


#***********User module***********

def User_logout(request):
    if 'U_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

#user index

def ind(request):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        user_count=Contact_messages.objects.filter(user_id=U_id).count()
        return render(request, 'User_index.html',{'mem1':mem1,'user_count':user_count})


def User_notification(request):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        user_reg = user_registration.objects.all()
        mess3 = Contact_messages.objects.filter(user_id=U_id)
        return render(request, 'User_notification.html',{'user_reg':user_reg,'mem1':mem1,'mess3':mess3}) 


def User_viewmatchresult(request):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        turf1 = Turf.objects.all()
        view = Matchresult.objects.all().order_by("-id")
        return render(request, 'User_viewmatchresult.html',{'turf1':turf1,'mem1':mem1,'view':view}) 


def User_contact(request):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        des2=designation.objects.get(designation="users")
        if request.method == 'POST':
            
            a = Contact_messages()
            a.name  = request.POST['name']
            a.email  = request.POST['email']
            a.message_type  = request.POST['messagetype']
            a.message  = request.POST['message']
            a.user_id  = U_id
            a.designation_id = des2.id
            a.save()
            msg_success = "Message send successfully"
            return render(request, 'owner_contactus.html', {'msg_success': msg_success})
        return render(request, 'User_contactus.html',{'mem1':mem1})