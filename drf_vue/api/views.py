from django.shortcuts import render
from students.models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('last_name')
    serializer_class = StudentSerializer