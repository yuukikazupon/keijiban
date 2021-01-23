from django.shortcuts import render,redirect
from .models import User
from .forms import KeijibanForm,SignupForm,ProfileForm,LoginForm,CreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def listfunc(request) :
    object_list = Keijiban.objects.all()
    return render(request,"list.html",{"object_list":object_list})

def createfunc(request) :
    if request.method == "POST" :
        keijiban = Keijiban()
        createform = CreateForm(request.POST,instance = keijiban)
        createform.instance.author_id = Profile.objects.get(pk=request.user.id-1).id
        createform.save()
        return redirect("list")


    else :
        createform = CreateForm()

        return render(request,"create.html",{"createform":createform})

def profilefunc(request) :
    if request.method == "POST" :
        profile = Profile()
        profileform = ProfileForm(request.POST,instance=profile)
        if profileform.is_valid() :
            profileform.save()
            return redirect("list")
    else :
        profileform = ProfileForm()
        return render(request,"profile.html",{"profileform":profileform})






def signupfunc(request) :

    if request.method == "POST" :
        signup = User()
        signupform = SignupForm(request.POST,instance=signup)
        profile = Profile()
        profileform = ProfileForm(request.POST,instance=profile)

        if signupform.is_valid():

            username1 = signupform.cleaned_data.get("username")
            password1 = request.POST["password"]
            password1_2=request.POST["password1_2"]
            if password1 == password1_2 :

                if profileform.is_valid() :
                    profileform.save()
                    User.objects.create_user(username1,"",password1)
                    return redirect("login")
                else :
                    return render(request,"signup.html",{"signupform":signupform,"profileform":profileform})
            else :
                return render(request,"signup.html",{"message":"パスワードを確認してください","signupform":signupform,"profileform":profileform})
        else :
            return render(request,"signup.html",{"message":"このユーザーは登録されています","signupform":signupform,"profileform":profileform})
    else :
        signupform = SignupForm()
        profileform = ProfileForm()
        return render(request,"signup.html",{ "signupform":signupform ,"profileform":profileform})


def loginfunc(request) :
    if request.method == "POST" :
        loginlogin = User()
        loginform = LoginForm(request.POST,instance = loginlogin)
        if loginform.is_valid() :
            return render(request,"login.html",{"message":"登録がありません。新規登録してください","loginform":loginform})
        else :
            username2 = request.POST["username"]
            password2 = request.POST["password"]
            user = authenticate(request,username=username2,password=password2)
            if user is not None :
                login(request,user)
                return redirect("list")
            else :
                return render(request,"login.html",{"message":"ユーザー名かパスワードが異なっております","loginform":loginform})
    else :
        loginform = LoginForm()
        return render(request,"login.html",{"loginform":loginform})

def chat(request):
    return render(request, 'chat.html', {})
