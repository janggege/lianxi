import json

from django.shortcuts import render

from api import Api
from . import controllers as account_ctl


class AppApi(Api):
    authenticator = authenticator


class LoginView(AppApi):
    need_authorize = False

    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        signture = account_ctl.login()

        data = {
            'signture': signture,
        }

        return data


class PlatformView(AppApi):

    def post(self, request):
        data = json.loads(request.body)

        name = data.get('name')
        sign = data.get('sign')
        if not name or not sign:
            return

        create_data = {
            'name': name,
            'sign': sign,
        }

        account_ctl.create_platform(**create_data)


class AccountView(AppApi):

    def post(self, request):
        data = json.loads(request.body)

        name = data.get('name')
        phone = data.get('phone')
        sex = data.get('sex')
        password = data.get('password')

        platform_ids = data.get('platform_ids')

        create_data = {
            'phone': phone,
            'password': password,
            'name': name,
            'sex': sex,
        }
        account = account_ctl.create_account(**create_data)
        if platform_ids:
            create_data = {
                'account_id': account.pk,
                'platform_ids': platform_ids,
            }
            account_ctl.create_account_to_platform_mapping(**create_data)
