from django.urls import path
from sleepApp import views

urlpatterns = [
    path('',views.UserApi.as_view()),
    path('login/username=<str:username>&password=<str:password>',views.AccountApi.as_view()),
    path('<str:Id>',views.UserApi.as_view()),
] 