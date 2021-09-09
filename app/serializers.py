from django.db import models
from django.db.models.fields import Field
from rest_framework import serializers
from .models import student

class student_serializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
