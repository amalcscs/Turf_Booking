import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
    req1 = Turf.objects.filter(designation_id=desig).order_by("-id")
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
        msg_success = "Reply send successfully"
        return render(request, 'Admin_notification.html',{'msg_success':msg_success})
    return redirect('Admin_notification')

def Admin_view_matches(request):
    team = Teams.objects.all()
    turf1 = Turf.objects.all()
    view = Matches.objects.all().order_by("-id")
    return render(request, 'Admin_view_matches.html',{'team':team,'view':view,'turf1':turf1})

def Admin_contact(request):
      return render(request, 'Admin_contact.html')

def Admin_signupdetails(request):
    userreg = user_registration.objects.all()
    return render(request, 'Admin_signupdetails.html',{'userreg':userreg})

def Admin_addowner(request,id):
    j = designation.objects.get(designation="owner")
    n = user_registration.objects.filter(id=id).update(designation_id = j.id)
    return redirect('Admin_signupdetails')

def Admin_update(request,id):
    c = user_registration.objects.get(id=id)
    
    return render(request, 'Admin_update.html',{'c':c})

def Admin_updatesave(request,id):
    if request.method == 'POST':
        d = user_registration.objects.get(id=id)
        d.Firstname   = request.POST.get('firstname')
        d.Lastname  = request.POST.get('lastname')
        d.place  = request.POST.get('place')
        d.address   = request.POST.get('address')
        d.pincode   = request.POST.get('pincode')
        d.mobile   = request.POST.get('mobile')
        d.email   = request.POST.get('email')
        d.photo = request.FILES['files']
        d.save()
        return redirect('Admin_signupdetails')


def Admin_delete(request,id):
    
        m = user_registration.objects.get(id=id)
        m.delete()
        return redirect('Admin_signupdetails')

def Admin_Turfbooking(request):
    trufbook = TurfBooking.objects.all()
    return render(request,'Admin_Turfbooking.html',{'trufbook':trufbook})

def Admin_Ticketbooking(request):
    ticketbook = Matches.objects.all()
    return render(request,'Admin_Ticketbooking.html',{'ticketbook':ticketbook})

def Admin_matchresult(request):
    turf1 = Turf.objects.all()
    view = Matchresult.objects.all().order_by("-id")
    return render(request,'Admin_matchresult.html',{'view':view,'turf1':turf1})









  


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
        dess = designation.objects.get(designation="owner")
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
            abc.designation_id = dess.id
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
            ab.matchname = request.POST['matchname']
            ab.firstteam = request.POST['firstteam']
            ab.secondteam = request.POST['secondteam']
            ab.date = request.POST['date']
            ab.fromtime = request.POST['time']
            ab.Ticketprice = request.POST['ticketprice']
            ab.photo = request.FILES['image']
            
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
        turf = Turf.objects.all()
        tems = Teams.objects.all()
        d = Matches.objects.all()
        if request.method == 'POST':
            
            an = Matchresult()
            an.turf_id   = request.POST['turfname']
            an.location_id  = request.POST['location']
            an.matchname  = request.POST['matchname']
            an.firstteam_id  = request.POST['firstteam']
            an.secondteam_id   = request.POST['secondteam']
            an.win_team_id   = request.POST['winteam']
            an.loss_team_id   = request.POST['lossteam']
            an.photo = request.FILES['image']
            an.date = request.POST['date']
            an.fromtime = request.POST['time']
            an.user_id  = O_id
            an.save()
            msg_success = "Match result Added successfull"
            return render(request, 'match_result.html', {'msg_success': msg_success})
        return render(request,'match_result.html',{'mem':mem,'turf':turf,'tems':tems,'d':d}) 


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


def Owner_Turf_bookingviewUser(request):
    if 'O_id' in request.session:
        if request.session.has_key('O_id'):
            O_id = request.session['O_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=O_id)
        desss = designation.objects.get(designation="users")
        turfbook = TurfBooking.objects.filter(designation_id = desss.id)
        return render(request, 'Owner_Turf_bookingviewUser.html',{'turfbook':turfbook,'mem':mem})

def Owner_accept_booking(request,id):
    n = TurfBooking.objects.filter(id=id).update(status = "booked")
    return redirect('Owner_Turf_bookingviewUser')

def Owner_reject_booking(request,id):
    n = TurfBooking.objects.filter(id=id).update(status = "rejected")
    return redirect('Owner_Turf_bookingviewUser')


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


def about(request):
    return render(request, 'aboutus.html')

#booking turf

def turf(request):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        allturf = Turf.objects.filter(status="approved") 
        return render(request, 'turfs.html',{'allturf':allturf,'mem1':mem1})


def books(request,id):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        design = designation.objects.get(designation="users")
        if request.method == 'POST':
            
            a = TurfBooking()
            a.date  = request.POST['date']
            a.fromtime  = request.POST['time']
            a.sport  = request.POST['Sport']
            a.gamestructure  = request.POST['game_structure']
            a.user_id  = U_id
            a.designation_id = design.id
            a.Turf_id = id
            a.save()
            msg_success = "Booking Request send successfully"
            return render(request, 'bookings.html', {'msg_success': msg_success})
        return render(request, 'bookings.html',{'mem1':mem1}) 


def Turf_booking(request):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        turfbook = TurfBooking.objects.filter(user_id = U_id)
        turfname = Turf.objects.filter(user_id = U_id)
        return render(request, 'Turf_booking.html',{'turfbook':turfbook,'mem1':mem1,'turfname':turfname})

def payment(request,id):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        design = designation.objects.get(designation="users")
        if request.method == 'POST':
            
            a = Payment.objects.get(id=id)
            a.date  = datetime.now()
            a.accountnumber  = request.POST['accnumber']
            a.bankname  = request.POST['bankname']
            a.ifsccode  = request.POST['ifsccode']
            a.branchname  = request.POST['branchname']
            a.amount  = request.POST['amount']
            a.user_id  = U_id
            a.designation_id = design.id
            a.Turf_id = id
            a.save()
            msg_success = "Paid"
            return render(request, 'Turf_booking.html', {'msg_success': msg_success})
        return render(request, 'Turf_booking.html',{'mem1':mem1}) 


def matches(request):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        team = Teams.objects.all()
        turf1 = Turf.objects.all()
        view = Matches.objects.all().order_by("-id")
        return render(request, 'matches.html',{'team':team,'mem1':mem1,'turf1':turf1,'view':view})

def book_ticket(request,id):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        turf = Turf.objects.all()
        order = Matches.objects.filter(id=id).order_by("-id")
        return render(request, 'book_ticket.html',{'mem1':mem1,'order':order,'turf':turf})

def ticket_booksave(request,id):
        if request.method == 'POST':
            
            a = Matches.objects.get(id=id)
            a.quantity  = request.POST['qty']
            a.total  = request.POST['item_total']
            a.accountnumber  = request.POST['accnumber']
            a.bankname  = request.POST['bankname']
            a.ifsccode  = request.POST['ifsccode']
            a.branchname  = request.POST['branchname']
            a.paymentdate  = datetime.now()
            a.paymentstatus  = "paid"
            a.save()
            return redirect('matches')

def ticket_bookpayment(request,id):
    if 'U_id' in request.session:
        if request.session.has_key('U_id'):
            U_id = request.session['U_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=U_id)
        return render(request,'ticket_bookpayment.html',{'mem1':mem1})
        # if request.method == 'POST':
            
        #     a = Payment.objects.get(id=id)
        #     a.accountnumber  = request.POST['qty']
        #     a.bankname  = request.POST['item_total']
        #     a.ifsccode  = request.POST['qty']
        #     a.branchname  = request.POST['item_total']
        #     a.date  = datetime.now()
        #     a.amount  = request.POST['item_total']
        #     a.user_id = U_id
        #     a.designation_id = des.id
        #     a.matches_id  = id
        #     a.save()
        #     return render(request,'ticket_bookpayment.html',{'mem1':mem1})
        

def bookingdelete(request,id):
    
        m = Matches.objects.get(id=id)
        m.delete()
        return redirect('matches')

def shop(request):
    shopcat = Shopcategory.objects.all()
    items = Shopitems.objects.all()
    return render(request, 'shoplist.html',{'shopcat':shopcat,'items':items})

def shopsave(request,id):
        if request.method == 'POST':
            a = Shopitems.objects.get(id=id)
            a.size = request.POST['size1']
            a.color = request.POST['color1']
            a.quantity = request.POST['quantity']
            a.finalprice = request.POST['rate']
            a.status = "cart"
            a.save()
            return redirect('shop')

def cart(request):
    shopcat = Shopcategory.objects.all()
    items = Shopitems.objects.all()
    return render(request, 'cart.html',{'shopcat':shopcat,'items':items})