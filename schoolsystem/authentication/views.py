from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
import json
from django.http import HttpResponse

class ValidateUser(View):
    def get(self,request):
        data  = json.loads(request.body)
        username = data['username']
        #turn it into a string
        if not str(username).isalnum():
            return JsonResponse({'username_error':'Username should not contain alpha nuneric'},status=400)
        if User.objects.filter(username=username).exists():             
            return JsonResponse({'username_valid':'User name in use, choose another one'},status=409)
        return JsonResponse({'username_valid':True})

class SignupView(View):
    def get(self,request):
        return render(request,'authentication/sign_up.html')

class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/index.html')
class LoginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')
class ForgotpasswordView(View):
    def get(self,request):
        return render(request,'authentication/forgotpassword.html')
