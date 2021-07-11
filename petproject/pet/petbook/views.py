from django.shortcuts import render, redirect
from .models import dog
from django.conf import settings
from .models import menudog
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.models import User, auth


# Create your views here.


def index(request):
    dogs = dog.objects.all

    return render(request, "index.html", {'dogs': dogs})


def booking(request):
    menud = menudog.objects.all
    return render(request, "booking.html", {'menud': menud})


def bookpet(request):
    current_user = request.user

    subject = "thank for your registration & join with our family"
    message = "welcome to petbook! choose ur pet book your correct neede puppies"
    from_email = settings.EMAIL_HOST_USER
    to_list = [current_user.email, settings.EMAIL_HOST_USER]
    email = EmailMessage(subject, message, from_email,
                         to_list)
    email.fail_silently = True
    email.send()
    return redirect("/")


def login(request):
    if request.method == 'POST':
        username = request.POST['usernamel']
        password = request.POST['passwordl']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentails')
            return redirect('account.html')
    else:
        return render(request, "account.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['usernames']
        password1 = request.POST['passwords1']
        password2 = request.POST['passwords2']
        email = request.POST['emails']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                user.save()
                subject = "thank for your registration & join with our family"
                message = "welcome to petbook! choose ur pet book your correct neede puppies"
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email, settings.EMAIL_HOST_USER]
                email = EmailMessage(subject, message, from_email,
                                     to_list)
                email.fail_silently = True
                email.send()
                messages.info(request, 'user created ')
        else:
            print("pass is not matching")
            messages.error(request, 'mismatch password')
            return redirect('register')
        return redirect('index.html')
    else:
        return render(request, "account.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
