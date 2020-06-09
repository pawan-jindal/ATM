from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

def get_and_authenticate_user(username, password):
	user = authenticate(username=username, password=password)
	if user is None:
		raise serializers.ValidationError("Invalid username/password. Please try again!")
	return user