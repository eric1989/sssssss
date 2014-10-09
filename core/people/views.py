from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate,login, logout

from people.models import User
class LoginView(View):

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

	def post(self, request):
		logout(request)
		return HttpResponse('success')

class RegisterView(View):

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
		finally:
			return HttpResponse('error')

