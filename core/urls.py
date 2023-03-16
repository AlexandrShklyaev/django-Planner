from django.urls import path, include
import core.views

urlpatterns = [

    path('signup', core.views.Users_Create_View.as_view(), name='signup'),
    path('login', core.views.Users_Login_View.as_view(), name='login'),
    path('profile', core.views.Users_Profile_View.as_view(), name='update-retrieve-destroy-user'),
    path('update_password', core.views.Users_Update_Password_View.as_view(), name='update-password'),



]