from django.shortcuts import get_object_or_404
from django.shortcuts import render
from . import views
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Id
from .serializers import IdSerializer

#from django.contrib.auth.models import student
def index_student(request):
    return HttpResponse("<h1>This is the student app homepage</h1>")

class IdList(APIView):

    def get(self, request):
        id = Id.objects.all()
        serializer = IdSerializer(id, many=True)
        return HttpResponse(serializer.data)




#class List_student(APIView):

#    authentication_classes = [authentication.TokenAuthentication]
#    permission_classes = [permissions.IsAdminUser]

#    def get(self, request, format=None):
#        students = [student.name for student in Student.objects.all()]
#        return Response(students)


#def index_student(request):
#    return HttpResponse("<h1>This is the student app homepage</h1>")
