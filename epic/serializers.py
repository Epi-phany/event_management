from rest_framework import serializers
#from django.contrib.auth import get_user_model
from .models import User
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

def validate_min_length(value):
    if len(value) < 6:
        raise ValidationError("your password should be 6 characters or more.")


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length=25)
    password = serializers.CharField(write_only=True,validators=[validate_min_length])

    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self,validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user