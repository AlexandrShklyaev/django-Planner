from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from core.models import User


class UserCreateModelSerializer(serializers.ModelSerializer):
    password_repeat = serializers.SerializerMethodField('get_pasw')
    def get_pasw(self, foo):
        return foo.password

    class Meta:
        model = User
        fields = ("id",
                  "username",
                  "first_name",
                  "last_name",
                  "email",
                  "password",
                  "password_repeat"
                  )

    def is_valid(self, *, raise_exception=False):
        data = self.initial_data
        self.pswrd_1 = data["password"]
        self.pswrd_2 = data["password_repeat"]

        validate_password(self.pswrd_1)

        if self.pswrd_1 and self.pswrd_2 and self.pswrd_1 != self.pswrd_2:
            return super().is_valid(raise_exception=True)
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UserLoginModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password',)

    def create(self, validated_data: dict):
        if not (user := authenticate(
                username=validated_data['username'],
                password=validated_data['password'],
        )):
            raise AuthenticationFailed
        return user


class User_DetailView_Model_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class User_Update_Password_Serializer(serializers.ModelSerializer):
    old_password = serializers.models.CharField(max_length=128)
    new_password = serializers.models.CharField(max_length=128)

    class Meta:
        model = User
        fields = ["old_password", "new_password"]

    def is_valid(self, *, raise_exception=False):
        data = self.initial_data
        new_password = data["new_password"]
        if validate_password(new_password):
            return super().is_valid(raise_exception=True)
        return super().is_valid(raise_exception=raise_exception)


