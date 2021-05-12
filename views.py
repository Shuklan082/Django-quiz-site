from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Already Taken')
                return redirect(request.path_info)
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Taken')
                return redirect(request.path_info)
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                subject = 'Yo BOI'
                message = 'Hi {{user.username}}, This IS DJANGO'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )
                return redirect('/')
        else:
            messages.error(request,'Password not Matching')
            return redirect(request.path_info)
    else:
        return render(request,'register.html')


    ###############################################

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect(request.path_info)
    else:
        return render(request,'quiz/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
