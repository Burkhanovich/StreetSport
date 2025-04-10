from rest_framework import serializers
from .models import Account
import re
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('id', 'name', 'phone_number', 'password1', 'password2')


    def validate_phone_number(self, value):
        if not re.match(r'^\+998\d{9}$', value):
            raise serializers.ValidationError("Telefon raqami formati noto‘g‘ri")
        return value

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("Parollar mos emas")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')

        user = Account(**validated_data)
        user.set_password(password)
        user.save()
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'role')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        data['name'] = self.user.name
        return data

class UpdateRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('role',)

class ManagerRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Account
        fields = ('id', 'name', 'phone_number', 'password1', 'password2')
        read_only_fields = ('id',)

    def validate_phone_number(self, value):
        if not re.match(r'^\+998\d{9}$', value):
            raise serializers.ValidationError("Telefon raqami formati noto‘g‘ri. Format: +998901234567")
        if Account.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Bu telefon raqami allaqachon ishlatilgan.")
        return value

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError({"password": "Parollar mos emas"})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')


        user = Account(
            phone_number=validated_data['phone_number'],
            name=validated_data.get('name', ''),
            role=3
        )
        user.set_password(password)
        user.save()
        return user








