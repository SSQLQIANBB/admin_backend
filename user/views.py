from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework_jwt.settings import api_settings

from user.models import SysUser, SysUserSerializer


def generate_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    assert isinstance(payload, object)
    return jwt_encode_handler(payload)
# Create your views here.
class LoginView(View):
    def post(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        try:
            user = SysUser.objects.get(username=username, password=password)
            data = SysUserSerializer(user).data
            token = generate_token(user)
        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'message': '用户名或密码错误'})
        return JsonResponse({'code': 200, 'message': 'success', 'data': {'token': token, **data }})

class TestView(View):

    def get(self, request):
        return JsonResponse({'code': 200, 'message': 'success'})

class UserView(View):

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            # sys_user = SysUser.objects.all()
            # user_list = list(sys_user.values())
            user_list = [model_to_dict(user) for user in SysUser.objects.all()]
            print(user_list)
            return JsonResponse({'code': 200, 'message': 'success', 'sys_user': user_list})
        else:
            return JsonResponse({'code': 401, 'message': 'no Authorization'})

class JwtView(View):
    def get(self, request):
        user = SysUser.objects.get(id=1)
        print(user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return JsonResponse({'code': 200, 'message': 'success', 'token': token})