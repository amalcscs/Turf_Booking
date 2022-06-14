
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
    re_path(r'^Forgot_password$',views.Forgot_password, name='Forgot_password'),
    re_path(r'^User_logout$',views.User_logout, name='User_logout'),
    
    re_path(r'^about/$',views.about, name='about'),
    re_path(r'^matches/$',views.matches, name='matches'),
    re_path(r'^shop/$',views.shop, name='shop'),
    re_path(r'^turf/$',views.turf, name='turf'),
    re_path(r'^cart/$',views.cart, name='cart'),
    re_path(r'^books/(?P<id>\d+)/$',views.books, name='books'),  
    re_path(r'^payment/$',views.payment, name='payment'),  
    re_path(r'^buy_tickets_readmore/$',views.buy_tickets_readmore, name='buy_tickets_readmore'),  
    re_path(r'^book_ticket/(?P<id>\d+)/$',views.book_ticket, name='book_ticket'),  
    re_path(r'^ticket_booksave/(?P<id>\d+)/$',views.ticket_booksave, name='ticket_booksave'),  
    re_path(r'^ticket_bookpayment/(?P<id>\d+)/$',views.ticket_bookpayment, name='ticket_bookpayment'),  
    re_path(r'^bookingdelete/(?P<id>\d+)/$',views.bookingdelete, name='bookingdelete'),  
    re_path(r'^User_contact/$',views.User_contact, name='User_contact'),  
    re_path(r'^Owner_notification/$',views.Owner_notification, name='Owner_notification'),  
    re_path(r'^User_notification/$',views.User_notification, name='User_notification'),  
    re_path(r'^User_viewmatchresult/$',views.User_viewmatchresult, name='User_viewmatchresult'),  
    re_path(r'^Turf_booking/$',views.Turf_booking, name='Turf_booking'),  
    re_path(r'^payment/(?P<id>\d+)/$',views.payment, name='payment'),  
    re_path(r'^shopsave/(?P<id>\d+)/$',views.shopsave, name='shopsave'),  
    re_path(r'^cartsave/(?P<id>\d+)/$',views.cartsave, name='cartsave'),  
    re_path(r'^cartpayment/(?P<id>\d+)/$',views.cartpayment, name='cartpayment'),  
    re_path(r'^cartpaymentsave/(?P<id>\d+)/$',views.cartpaymentsave, name='cartpaymentsave'),  
    re_path(r'^User_myorders/$',views.User_myorders, name='User_myorders'),  
    re_path(r'^User_changepassword/(?P<id>\d+)/$',views.User_changepassword, name='User_changepassword'),  

    re_path(r'^indexo/$',views.indexo, name='indexo'),
    re_path(r'^$',views.log, name='log'),
    re_path(r'^sign/$',views.sign, name='sign'),
    re_path(r'^add/$',views.add, name='add'),
    re_path(r'^Owner_Turf_edit/$',views.Owner_Turf_edit, name='Owner_Turf_edit'),
    re_path(r'^Owner_Team_edit/$',views.Owner_Team_edit, name='Owner_Team_edit'),
    re_path(r'^addteam/$',views.addteam, name='addteam'),
    re_path(r'^Owner_Match_edit/$',views.Owner_Match_edit, name='Owner_Match_edit'),
    re_path(r'^OwnerTurfdelete/(?P<id>\d+)/$',views.OwnerTurfdelete, name='OwnerTurfdelete'),
    re_path(r'^OwnerMatchesdelete/(?P<id>\d+)/$',views.OwnerMatchesdelete, name='OwnerMatchesdelete'),
    re_path(r'^OwnerTeamdelete/(?P<id>\d+)/$',views.OwnerTeamdelete, name='OwnerTeamdelete'),
    re_path(r'^Turf_Edit/(?P<id>\d+)/$',views.Turf_Edit, name='Turf_Edit'),
    re_path(r'^Turf_Edit_save/(?P<id>\d+)/$',views.Turf_Edit_save, name='Turf_Edit_save'),
    re_path(r'^Team_Edit/(?P<id>\d+)/$',views.Team_Edit, name='Team_Edit'),
    re_path(r'^Team_Edit_save/(?P<id>\d+)/$',views.Team_Edit_save, name='Team_Edit_save'),
    re_path(r'^Match_Edit/(?P<id>\d+)/$',views.Match_Edit, name='Match_Edit'),
    re_path(r'^Match_Edit_save/(?P<id>\d+)/$',views.Match_Edit_save, name='Match_Edit_save'),
    re_path(r'^OwnerMatcheResultdelete/(?P<id>\d+)/$',views.OwnerMatcheResultdelete, name='OwnerMatcheResultdelete'),
    re_path(r'^MatchResult_Edit_Save/(?P<id>\d+)/$',views.MatchResult_Edit_Save, name='MatchResult_Edit_Save'),
    re_path(r'^MatchResult_Edit/(?P<id>\d+)/$',views.MatchResult_Edit, name='MatchResult_Edit'),
    re_path(r'^OwnerShoppingCategorydelete/(?P<id>\d+)/$',views.OwnerShoppingCategorydelete, name='OwnerShoppingCategorydelete'),
    re_path(r'^ShoppingCategory_Edit/(?P<id>\d+)/$',views.ShoppingCategory_Edit, name='ShoppingCategory_Edit'),
    re_path(r'^ShoppingCategory_Edit_save/(?P<id>\d+)/$',views.ShoppingCategory_Edit_save, name='ShoppingCategory_Edit_save'),
    re_path(r'^OwnerShoppingItemdelete/(?P<id>\d+)/$',views.OwnerShoppingItemdelete, name='OwnerShoppingItemdelete'),
    re_path(r'^ShoppingItem_Edit_save/(?P<id>\d+)/$',views.ShoppingItem_Edit_save, name='ShoppingItem_Edit_save'),
    re_path(r'^ShoppingItem_Edit/(?P<id>\d+)/$',views.ShoppingItem_Edit, name='ShoppingItem_Edit'),
    re_path(r'^Owner_ShopItem_Edit/$',views.Owner_ShopItem_Edit, name='Owner_ShopItem_Edit'),
    
    re_path(r'^Owner_MatchResult_edit/$',views.Owner_MatchResult_edit, name='Owner_MatchResult_edit'),
    re_path(r'^Owner_ShoppingCategory_Edit/$',views.Owner_ShoppingCategory_Edit, name='Owner_ShoppingCategory_Edit'),
    re_path(r'^regis/$',views.regis, name='regis'),
    re_path(r'^req/$',views.req, name='req'),
    re_path(r'^Owner_book_details/$',views.Owner_book_details, name='Owner_book_details'),
    re_path(r'^Add_match/$',views.Add_match, name='Add_match'),
    re_path(r'^Owner_addshopcategory/$',views.Owner_addshopcategory, name='Owner_addshopcategory'),
    re_path(r'^Owner_addshopitem/$',views.Owner_addshopitem, name='Owner_addshopitem'),
    re_path(r'^match_result/$',views.match_result, name='match_result'),
    re_path(r'^Owner_contact/$',views.Owner_contact, name='Owner_contact'),
    re_path(r'^Owner_Turf_bookingviewUser/$',views.Owner_Turf_bookingviewUser, name='Owner_Turf_bookingviewUser'),
    re_path(r'^Owner_logout/$',views.Owner_logout, name='Owner_logout'),
    re_path(r'^Owner_messagereply/(?P<id>\d+)/$',views.Owner_messagereply, name='Owner_messagereply'),
    re_path(r'^Owner_accept_booking/(?P<id>\d+)/$',views.Owner_accept_booking, name='Owner_accept_booking'),
    re_path(r'^Owner_reject_booking/(?P<id>\d+)/$',views.Owner_reject_booking, name='Owner_reject_booking'),
    re_path(r'^Owner_senddate/(?P<id>\d+)/$',views.Owner_senddate, name='Owner_senddate'),
    re_path(r'^Owner_changepassword/(?P<id>\d+)/$',views.Owner_changepassword, name='Owner_changepassword'),
    re_path(r'^Owner_senddeliverydate/$',views.Owner_senddeliverydate, name='Owner_senddeliverydate'),
    re_path(r'^Owner_viewticketbooking/$',views.Owner_viewticketbooking, name='Owner_viewticketbooking'),
    re_path(r'^Owner_adminrepliedmessages/$',views.Owner_adminrepliedmessages, name='Owner_adminrepliedmessages'),

    re_path(r'^Admin_index/$',views.Admin_index, name='Admin_index'),
    re_path(r'^Admin_changepassword/$',views.Admin_changepassword, name='Admin_changepassword'),
    re_path(r'^Admin_signupdetails/$',views.Admin_signupdetails, name='Admin_signupdetails'),
    re_path(r'^Admin_logout/$',views.Admin_logout, name='Admin_logout'),
    re_path(r'^Admin_Turf_requests/$',views.Admin_Turf_requests, name='Admin_Turf_requests'),
    
    re_path(r'^Admin_notification/$',views.Admin_notification, name='Admin_notification'),
    re_path(r'^Admin_messagereply/(?P<id>\d+)/$',views.Admin_messagereply, name='Admin_messagereply'),
    re_path(r'^Admin_view_matches/$',views.Admin_view_matches, name='Admin_view_matches'),
    re_path(r'^Admin_contact/$',views.Admin_contact, name='Admin_contact'),
    re_path(r'^AdminTurfapprove/(?P<id>\d+)/$',views.AdminTurfapprove, name='AdminTurfapprove'),
    re_path(r'^AdminTurfrejected/(?P<id>\d+)/$',views.AdminTurfrejected, name='AdminTurfrejected'),
    re_path(r'^Admin_addowner/(?P<id>\d+)/$',views.Admin_addowner, name='Admin_addowner'),
    re_path(r'^Admin_update/(?P<id>\d+)/$',views.Admin_update, name='Admin_update'),
    re_path(r'^Admin_updatesave/(?P<id>\d+)/$',views.Admin_updatesave, name='Admin_updatesave'),
    re_path(r'^Admin_delete/(?P<id>\d+)/$',views.Admin_delete, name='Admin_delete'),
    re_path(r'^Admin_Turfbooking/$',views.Admin_Turfbooking, name='Admin_Turfbooking'),
    re_path(r'^Admin_Ticketbooking/$',views.Admin_Ticketbooking, name='Admin_Ticketbooking'),
    re_path(r'^Admin_matchresult/$',views.Admin_matchresult, name='Admin_matchresult'),
    re_path(r'^Admin_viewshopping/$',views.Admin_viewshopping, name='Admin_viewshopping'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
