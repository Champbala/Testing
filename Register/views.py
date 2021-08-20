
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth




# Create your views here.


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')       



def setcookie(request):
    html=HttpResponse("<h1>Dataflair Django tutoial</h1>")
    html.set_cookie('dataflair',"Hello this your cookies",max_age=None)
    return html

def setcookie(request):
    html=HttpResponse("<h1>Dataflair Django tutoial</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair',"Welcomeback")
        value=int(request.COOKIES.get('visits'))
        html.set_cookie('vistss',value+1)
    else:
        value=1
        text="welcome for the firts time"
        html.set_cookie('visits',value)
        html.set_cookie('dataflair',text)
    return html

def showcookie(request):
    # show=request.COOKIES['dataflair']
    # html="<h1>{0}</h1>".format(show)
    # return HttpResponse(html)
    if request.COOKIES.get('visits'):
        value=request.COOKIES.get('visits')
        text=request.COOKIES.get('dataflair')
        html=HttpResponse("<h1>{0}you have requested this page {1}times</h1>".format(text,value))
        html.set_cookie('visits',int(value)+1)
        return html
    else:
        return redirect('/setcooki')


def delete(request):
    if request.COOKIES.get('visits'):
        response =HttpResponse("<h1>cookies deleted </h1>")
        response.delete_cookie('visits')
    else:
        response =HttpResponse("<h1>cookies need to be create </h1>")
    return response


    
