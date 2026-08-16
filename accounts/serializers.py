from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import get_tokens_for_user
from .models import ChronicCondition, UserCondition
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # U dont pass a toekn in register go to view
    first_name=serializers.CharField( 
        required=True,
        max_length=150
        )
    last_name=serializers.CharField(
        required=True,
        max_length=150
    )
    
    email=serializers.EmailField(required=True)
    username=serializers.CharField()
    password=serializers.CharField(
        write_only=True,
        min_length=8,
        required=True
    )
    confirm_password = serializers.CharField(
        required=True,
        write_only=True,
        min_length=8
        )
    class Meta:
        model=User
        fields=(
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "confirm_password",
        )
    def validate(self, attrs):
        attrs["first_name"]=attrs["first_name"].strip()
        attrs["email"]=attrs["email"].strip()
        
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"detail":"Passwords do not match"},)
        
        return attrs
    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user=User.objects.create_user(**validated_data)
        return user

class LogInSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True,)
    password=serializers.CharField(
        required=True,
        write_only=True)
    class Meta:
        model=User
        fields=("email","password")
    def validate(self, attrs):
        attrs["email"]=attrs["email"].strip()
        try:
            user=User.objects.get(email=attrs["email"])
            attrs["token"]=get_tokens_for_user(user=user)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "Invalid credentials."})
        if not user or  not user.check_password(attrs["password"]):
            raise serializers.ValidationError({"detail": "Invalid credentials."})
        return attrs["token"]
class ChronicConditionSerializer(serializers.Serializer):
    class Meta:
        model=ChronicCondition
        fields = ["id", "name"]

class UserConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserCondition
        fields=["chronic_condition"]
    def create(self, validated_data):
        user_condition, created = UserCondition.objects.get_or_create(**validated_data)
        return user_condition