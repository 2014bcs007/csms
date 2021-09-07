from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('', csrf_exempt(LoginView.as_view()), name='login'),
   # path('login',views.login,name='login'),
    path('sign_up',csrf_exempt(SignupView.as_view()),name='sign_up'),
    path('ValidateUser',csrf_exempt(ValidateUser.as_view()),name='ValidateUser'),
    path('forgot_password',csrf_exempt(ForgotpasswordView.as_view()),name='forgot_password'),
]