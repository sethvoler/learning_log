"""定义users的URL模式"""
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
  # 登录页面
  path('login/', LoginView.as_view(template_name='login.html'), name='login'),

  # 注销
  path('logout/', views.logout_view, name='logout')
]
