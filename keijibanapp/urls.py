from django.urls import path
from .views import listfunc,signupfunc,loginfunc,createfunc,profilefunc,chat
from django.conf.urls import url

urlpatterns = [
    path("",signupfunc,name="signup"),
    path("login/",loginfunc,name="login"),
    path("list/",listfunc,name="list"),
    path("create/",createfunc,name="create"),
    path("profile/",profilefunc,name="profile"),
    path('chat/',chat, name='chat'),



]
