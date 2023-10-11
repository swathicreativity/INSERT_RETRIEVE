from django.urls import path
from . import views

urlpatterns = [    
    path("",views.signin,name="signin"),
    path('signin_verification',views.signin_verification,name="signin_verification"),
    path('otp_verification',views.otp_verification,name="otp_verification"),
    path("secure",views.secure,name="secure"), 
    path('create/', views.create_blog, name='create-blog'),
    path('show/', views.show_blogs, name='show_blogs'),   
    path('logout_page',views.logout_page,name='logout_page'),
]
