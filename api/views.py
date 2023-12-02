from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.response import Response


def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            student = Student.objects.get(id = id)
            serializer = StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return Response(json_data, content_type='application/json')
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return Response(json_data, content_type='application/json')