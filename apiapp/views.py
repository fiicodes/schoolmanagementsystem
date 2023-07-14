from adminapp.models import *
import os

import random
import string
from django.conf import settings
from django.core.mail import send_mail
import hashlib
import datetime
from django.http import JsonResponse
from apiapp.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



from rest_framework import permissions


@api_view(['GET'])

def teacherlist(request):
    #get all teachers
    #serialize them
    # return json

    t=teacher_tb.objects.all()
    serializer=teacherSerializer(t,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def addteacher(request):

     serializer=teacherSerializer(data=request.data)
     if serializer.is_valid():
       serializer.save()
     return Response(serializer.data)
@api_view(['GET'])

def courselist(request):
    #get all teachers
    #serialize them
    # return json

    c=course_tb.objects.all()
    serializer=courseSerializer(c,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def addcourseapi(request):

     serializer=courseSerializer(data=request.data)
     if serializer.is_valid():
       serializer.save()
     return Response(serializer.data)
@api_view(['GET','PUT','DELETE'])
def coursedetail(request,id):
 try:
    course=course_tb.objects.get(pk=id)
 except course_tb.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
 if request.method=='GET':
    serializer=courseSerializer(course)
    return Response(serializer.data)
 elif request.method=='PUT':
    serializer=courseSerializer(course,data=request.data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
 elif request.method=='DELETE':
     course.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)
 



# Create your views here.
