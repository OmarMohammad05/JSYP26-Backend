from django.urls import path 
from . import views
from rest_framework_simplejwt.views import TokenRefreshSlidingView
urlpatterns =[
    path("register/",views.RegisterView.as_view(),name="register"),
    path("login/",views.LogInView.as_view(),name="login"),
    path("token/refresh/",TokenRefreshSlidingView.as_view(),name="token_refresh"),
    path("user-condition/",views.UserConditionView.as_view(), name="user-condition"),
    path("conditions/", views.ConditionListView.as_view(),name="condition") # get الامراض يعمي عشان يختار
]