from django.contrib import admin
from django.urls import path
from Myposapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginForm ,name='loginform'),
    path('regis', views.Register),

    path('login', views.login),
    path('loginForm', views.loginForm),

    path('product/', views.product , name='product'),
    path('product/add_product/', views.add_Product),
    path('product/search/', views.search_product),
    path('product/edit_product/<str:pk>/', views.edit_Product),
    path('product/del_product/<str:pk>/', views.del_Product),

    path('promotion/', views.promotion),
    path('promotion/additem_promotion/', views.additem_promotion),
    path('promotion/delete_promotion/<str:pk>/', views.delete_promotion,name='deletePromotion'),
    path('promotion/delete_item/<str:pk>/', views.deleteitem_promotion,name='deleteItemPM'),
    path('promotion/view/<str:pk>/', views.promotion_view),
    path('promotion/history/<str:pk>/', views.history_view),
    path('promotion/history/', views.history_promotion),
    path('promotion/discount/', views.promotion_discount),
    path('promotion/buyXGetY/', views.promotion_buyXGetY),
    path('promotion/comboset/', views.promotion_comboset),
    path('promotion/atlest/', views.promotion_atlest),
    
    path('membership_promotion/', views.Membership_promotion),
    path('membership_promotion/point_set/', views.Membership_promotion_point_set),
    path('membership_promotion/point_history/', views.Membership_History_promotion_point),
    path('membership_promotion/rate_history/', views.Membership_History_promotion_rate),
    path('membership_promotion/history/', views.Membership_History_promotion),
    path('membership_promotion/addpromotion/discount/', views.Membership_promotion_discount),
    path('membership_promotion/addpromotion/discount2/', views.Membership_promotion_discount2),

    path('employee/', views.employee),
    path('employee/add_employee/', views.AddEmployee),
    path('employee/search/', views.Search_Employee),
    path('employee/edit_employee/<str:pk>/', views.edit_employee),
    path('employee/del_employee/<str:pk>/', views.del_employee),

    path('membership/', views.Membership),
    path('membership/add_membership/', views.add_Membership),
    # path('membership/search/', views.Search_Member),
    path('membership/edit_membership/<str:pk>/', views.edit_Membership),
    path('membership/del_membership/<str:pk>/', views.del_Membership),
    path('membership/search_membership', views.Search_Membership),
    # path('membership/del_membership/<str:pk>/', views.del_member),
    
    
    path('sales_report/', views.Sales_report),
    path('daily_report/', views.Daily_report),
    path('sales_history/', views.Sales_history),
    path('sales_history/bill_info/<str:pk>/', views.Bill_info,name='bill'),
    path('sales_history/Date/', views.Check_history_Date,name='bill'),
    path('sales_history/ID/', views.Check_history_ID,name='bill'),
    path('document/', views.Document),
    path('document/Date/', views.Document_Date),
    path('document/Tax_report/', views.Tax_report),

    path('finance/', views.Sales_report),
    
    path('cashier/', views.Cashier_mode),
    path('cashier/create_bill/', views.Create_Bill),
    path('cashier/success/', views.Cashier_success),
    path('cashier/delete_item/<str:pk>/',views.delete_product_bill),
    path('cashier/receipt/',views.C_Sales_history),
    path('cashier/receipt/<str:pk>/', views.C_Bill_info,name='bill'),
    
    path('logout/', views.Logout),

    path('logout/', views.Logout , name='logout'),

]
