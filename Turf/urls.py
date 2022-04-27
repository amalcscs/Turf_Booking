
from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from Turf_app import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^ind$',views.ind, name='ind'),
    
    re_path(r'^about/$',views.about, name='about'),
    re_path(r'^matches/$',views.matches, name='matches'),
    re_path(r'^shop/$',views.shop, name='shop'),
    re_path(r'^turf/$',views.turf, name='turf'),
    re_path(r'^cart/$',views.cart, name='cart'),
    re_path(r'^books/$',views.books, name='books'),  
    re_path(r'^payment/$',views.payment, name='payment'),  
    re_path(r'^buy_tickets_readmore/$',views.buy_tickets_readmore, name='buy_tickets_readmore'),  
    re_path(r'^book_ticket/$',views.book_ticket, name='book_ticket'),  
    re_path(r'^User_contact/$',views.User_contact, name='User_contact'),  
    re_path(r'^Owner_notification/$',views.Owner_notification, name='Owner_notification'),  
    re_path(r'^User_notification/$',views.User_notification, name='User_notification'),  

    re_path(r'^$',views.indexo, name='indexo'),
    re_path(r'^log/$',views.log, name='log'),
    re_path(r'^sign/$',views.sign, name='sign'),
    re_path(r'^add/$',views.add, name='add'),
    re_path(r'^addteam/$',views.addteam, name='addteam'),
    
    re_path(r'^regis/$',views.regis, name='regis'),
    re_path(r'^req/$',views.req, name='req'),
    re_path(r'^Owner_book_details/$',views.Owner_book_details, name='Owner_book_details'),
    re_path(r'^Add_match/$',views.Add_match, name='Add_match'),
    re_path(r'^match_result/$',views.match_result, name='match_result'),
    re_path(r'^Owner_contact/$',views.Owner_contact, name='Owner_contact'),

    re_path(r'^Admin_index/$',views.Admin_index, name='Admin_index'),
    re_path(r'^Admin_Turf_requests/$',views.Admin_Turf_requests, name='Admin_Turf_requests'),
    re_path(r'^Admin_notification/$',views.Admin_notification, name='Admin_notification'),
    re_path(r'^Admin_view_matches/$',views.Admin_view_matches, name='Admin_view_matches'),
    re_path(r'^Admin_contact/$',views.Admin_contact, name='Admin_contact'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
