from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from user.models import SysUser


# Create your views here.
class TestView(View):

    def get(self, request):
        return JsonResponse({'code': 200, 'message': 'success'})

class UserView(View):

    def get(self, request):
        # sys_user = SysUser.objects.all()
        # user_list = list(sys_user.values())
        user_list = [model_to_dict(user) for user in SysUser.objects.all()]
        print(user_list)
        return JsonResponse({'code': 200, 'message': 'success', 'sys_user': user_list})