from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import User
from core.serializers import UserCreateModelSerializer, User_Update_Password_Serializer, \
    User_DetailView_Model_Serializer, UserLoginModelSerializer
from django.contrib.auth import login, get_user, logout
import json


class Users_Create_View(CreateAPIView):
    serializer_class = UserCreateModelSerializer


class Users_Login_View(CreateAPIView):
    serializer_class = UserLoginModelSerializer

    def perform_create(self, serializer):
        login(request=self.request, user=serializer.save())
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Users_Profile_View(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = User_DetailView_Model_Serializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        try:
            logout(request)
        except:
            return JsonResponse({}, status=500)
        return JsonResponse({}, status=204)


class Users_Update_Password_View(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = User_Update_Password_Serializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        l_u = get_user(self.request)
        l_data = json.loads(request.body)
        old_password = l_data['old_password']
        new_password = l_data['new_password']
        if not self.get_object().check_password(old_password):
            raise ValidationError({'old_password': 'field is incorrect'})
        l_u.set_password(new_password)
        l_u.save()
        rez = JsonResponse({"old_password": old_password, "new_password": new_password}, status=200)
        return rez

    def patch(self, request, *args, **kwargs):
        l_u = get_user(self.request)
        l_data = json.loads(request.body)
        old_password = l_data['old_password']
        new_password = l_data['new_password']
        if not self.get_object().check_password(old_password):
            raise ValidationError({'old_password': 'field is incorrect'})
        l_u.set_password(new_password)
        l_u.save()
        rez = JsonResponse({"old_password": old_password, "new_password": new_password}, status=200)
        return rez
