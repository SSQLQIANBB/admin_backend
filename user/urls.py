from django.urls import path

from user.views import TestView, UserView, JwtView

app_name = 'user'
urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('list/', UserView.as_view(), name='user'),
    path('jwt/', JwtView.as_view(), name='login'),
]