from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate,login, logout

from people.forms import LoginForm, RegisterForm
from people.models import User
class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'people/login.html', {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('success')
            else:
                return HttpResponse('fail')
        else:
            return HttpResponse('user is none')

class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            return render(request, 'people/logout.html', {})
        else:
            return HttpResponse('not login')

    def post(self, request):
        logout(request)
        return HttpResponse('success')

class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        print "hi"
        return render(request, 'people/register.html', {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email    = request.POST['email']
        try:
            user = User.create_user(username=username,password=password,email=email)
        except Exception, e:
            raise("Cannot create_user")
        else:
            return HttpResponse('success')

