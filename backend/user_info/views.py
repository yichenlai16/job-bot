from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from urllib.parse import urlencode
from django.shortcuts import render
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from .models import User_Info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import requests
from .verify import decode_id_token
from .serializers import (
    MyTokenObtainPairSerializer,
    User_InfoSerializer,
    AuthUserSerializer,
    UserDetailSerializer,
    UserRegisterSerializer,
    UserSerializer,
)
from user_info.permissions import IsSelfOrReadOnly
from django.core import serializers

# Create your views here.
import logging
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action

from user_info.permissions import IsSelfOrReadOnly
import re


class UserSelfViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    lookup_field = "username"

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]

        return super().get_permissions()

    @action(detail=True, methods=["get"])
    def info(self, request, username=None):
        queryset = User.objects.get(username=username)
        serializer = UserDetailSerializer(queryset, many=False)
        return Response(serializer.data)

    @action(detail=False)
    def sorted(self, request):
        users = User.objects.all().order_by("-username")

        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)


class User_InfoViewSet(viewsets.ModelViewSet):
    queryset = User_Info.objects.all()
    serializer_class = User_InfoSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]

        return super().get_permissions()


class TestUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'uid'

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]

        return super().get_permissions()


class NotifyTest(APIView):
    def get(self, request):
        users = User.objects.get(username=request.user)
        user_info = User_Info.objects.get(user=users.id)
        notify_token = user_info.notify_token
        headers = {"Authorization": "Bearer " + notify_token}
        params = {"message": "測試訊息"}
        requests.post(
            "https://notify-api.line.me/api/notify", headers=headers, params=params
        )
        return HttpResponse("done")


class Notify(APIView):
    def get(self, request):
        users = User.objects.get(username=request.user)
        user_info = User_Info.objects.get(user=users.id)

        array_result = serializers.serialize("json", [user_info], ensure_ascii=True)
        just_object_result = array_result[1:-2]
        # print(users.filter('id'))
        # print(users.id)
        # print(user_info)
        return HttpResponse(just_object_result)


class NotifyToggle(APIView):
    def post(self, request):
        users = User.objects.get(username=request.user)
        user_info = User_Info.objects.get(user=users.id)
        print(user_info.notification)
        if user_info.notification == False:
            user_info.notification = True
            user_info.save()
            return HttpResponse(user_info.notification)
        else:
            user_info.notification = "False"
            user_info.save()
            return HttpResponse(user_info.notification)


class LineNotifyCallback(APIView):
    def get(self, request):
        pattern = "code=.*&"

        raw_uri = request.get_raw_uri()
        print(raw_uri)
        codes = re.findall(pattern, raw_uri)
        for code in codes:
            code = code[5:-1]
            print(code)

        code = request.GET.get("code")

        user_notify_token_get_url = "https://notify-bot.line.me/oauth/token"
        params = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.LINE_NOTIFY_URI,  # 這邊改成自己的https://ngrok domain/notify
            "client_id": settings.LINE_NOTIFY_ID,  # 這邊改成自己的Notify client_id
            "client_secret": settings.LINE_NOTIFY_SECRET,  # 這邊改成自己的Notify client_secret
        }
        print(params)
        get_token = requests.post(user_notify_token_get_url, params=params)
        token = get_token.json()["access_token"]
        user_info_url = "https://notify-api.line.me/api/status"
        headers = {"Authorization": "Bearer " + token}
        get_user_info = requests.get(user_info_url, headers=headers)
        print(get_user_info.json())
        notify_user_info = get_user_info.json()
        if notify_user_info["targetType"] == "USER":
            User_Info.objects.filter(name=notify_user_info["target"]).update(
                notify_token=token
            )
        elif notify_user_info["targetType"] == "GROUP":
            pass
        return HttpResponse()


class LineUrl(APIView):
    # permission_classes = (AllowAny)
    def post(self, request):
        r_uri = settings.LINE_LOGIN_URI
        client = settings.LINE_LOGIN_CLIENT_ID
        state = "nostate"  # it will be random value
        uri = f"https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id={client}&redirect_uri={r_uri}&scope=profile%20openid%20email&state={state}&initial_amr_display=lineqr"
        return Response({"code": "0", "msg": "成功", "data": {"url": uri}})


class LineLiffCallback(APIView):
    def post(self, request):
        access_token = request.data.get("access_token")
        if access_token == None:
            return Response({"code": "400", "msg": "?", "data": "?"})

        client_id = settings.LINE_LOGIN_CLIENT_ID
        line_verify_response = requests.get(
            "https://api.line.me/oauth2/v2.1/verify",
            params={"access_token": access_token},
        ).json()

        if line_verify_response.get("client_id") != client_id:
            return Response({"code": "400", "msg": "step 1 failed"})

        line_profile_response = requests.get(
            "https://api.line.me/v2/profile",
            headers={"Authorization": "Bearer " + str(access_token)},
        ).json()

        if line_profile_response.get("message") != None:
            return Response({"code": "400", "msg": "step 2 failed"})

        userId = line_profile_response.get("userId")
        displayName = line_profile_response.get("displayName")
        pictureUrl = line_profile_response.get("pictureUrl")

        try:
            user = User.objects.get(username=userId)
        except User.DoesNotExist:
            user = User(username=userId)
            user.set_unusable_password()
            user.save()

        try:
            oauth_user = User_Info.objects.get(uid=userId)
        except Exception as e:
            oauth_user = None

        if oauth_user:
            oauth_user.name = displayName
            oauth_user.pic_url = pictureUrl
            oauth_user.save()

        else:
            oauth_user = User_Info(
                user=user,
                uid=userId,
                name=displayName,
                pic_url=pictureUrl,
            )
            oauth_user.save()

        def get_tokens_for_user(user):
            refresh = RefreshToken.for_user(user)

            return {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

        return Response(
            {
                "token": get_tokens_for_user(user),
                "displayName": displayName,
                "pictureUrl": pictureUrl,
                "userId": userId,
            }
        )


# class LineNotifyCallback(APIView):

#     def post(self, request):
#         access_token = request.data.get('access_token')
#         if access_token == None:
#             return Response({'code': '400', 'msg': '?', 'data': '?'})

#         client_id = settings.LINE_LOGIN_CLIENT_ID
#         line_verify_response = requests.get(
#             "https://api.line.me/oauth2/v2.1/verify", query={'access_token': access_token}).json()

#         if line_verify_response.get('client_id') != client_id:
#             return Response({'code': '400', 'msg': 'step 1 failed'})

#         line_profile_response = requests.get(
#             "https://api.line.me/v2/profile", headers={'Authorization': 'Bearer '+str(access_token)}).json()

#         userId = line_profile_response.get('userId')
#         displayName = line_profile_response.get('displayName')
#         pictureUrl = line_profile_response.get('pictureUrl')

#         r_uri = settings.LINE_LOGIN_URI
#         secret = settings.LINE_LOGIN_SECRET
#         data = {
#             'client_id': client_id,
#             'client_secret': secret,
#             'grant_type': 'authorization_code',
#             'code': access_token,
#             'redirect_uri': r_uri
#         }
#         headers = {"Content-Type": "application/x-www-form-urlencoded"}
#         token_data = requests.post(
#             "https://api.line.me/oauth2/v2.1/token",
#             data=data, headers=headers
#         ).json()

#         # 解JWT
#         token = token_data.get('id_token')

#         if token is None:
#             return Response({'code': '400', 'msg': token_data['error_description'], 'data': '?'})

#         try:
#             verify_result = (decode_id_token(token, client_id, secret))
#             logging.info(str(verify_result))
#         except Exception as e:
#             logging.info(str(e))
#             return exceptions.AuthenticationFailed(detail='Could not validate credentials', code=None)

#         # 新增會員資料

#         line_uid = verify_result.get('sub')
#         line_name = verify_result.get('name')
#         line_picture = verify_result.get('picture')
#         email = verify_result.get('email')

#         access_token = token_data.get('access_token')
#         access_token_expired_at = token_data.get('expires_in')
#         refresh_token = token_data.get('refresh_token')
#         refresh_token_expired_at = token_data.get('expires_in')

#         try:
#             user = User.objects(username=line_uid)
#         except User.DoesNotExist:
#             user = User(username=line_uid)
#             user.set_unusable_password()
#             user.save()

#         try:
#             oauth_user = User_Info.objects.get(uid=line_uid)
#         except Exception as e:
#             oauth_user = None

#         if oauth_user:
#             oauth_user.name = line_name
#             oauth_user.pic_url = line_picture
#             oauth_user.save()

#         else:
#             oauth_user = User_Info(
#                 user=user.id,
#                 uid=line_uid,
#                 name=line_name,
#                 pic_url=line_picture,
#             )
#             oauth_user.save()

#         user.backend = 'django.contrib.auth.backends.ModelBackend'
#         login(request, user)

#         return{
#             'access_token': access_token,
#             'refresh_token': refresh_token
#         }
