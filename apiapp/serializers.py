from rest_framework import serializers
from adminapp.models import *
class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=teacher_tb
        fields='__all__' 
class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model=course_tb
        fields='__all__' 