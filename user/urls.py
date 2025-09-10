from django.urls import path

from user.views import TestView, UserView

app_name = 'user'
urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('list/', UserView.as_view(), name='user'),
]