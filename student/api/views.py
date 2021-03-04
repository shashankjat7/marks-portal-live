from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from student.models import student

from .serializers import studentSerializer
@api_view(['POST', ])
def submit_marks_view(request):
    if request.method == 'POST':
        serializer = studentSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            student = serializer.save()
            data['response'] = 'SUCCESSFULLY REGISTERED MARKS'
            data['roll_no'] = student.roll_no
            data['name'] = student.name
            data['marks_maths'] = student.marks_maths
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET', ])
def get_students(request):
    try:
        students = student.objects.order_by('-percentage')

    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentSerializer(students,many=True)
        return Response(serializer.data)

@api_view(['GET', ])
def get_students_reverse(request):
    try:
        students = student.objects.order_by('percentage')

    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentSerializer(students,many=True)
        return Response(serializer.data)

@api_view(['GET', ])
def get_students_roll(request):
    try:
        students = student.objects.order_by('roll_no')

    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentSerializer(students,many=True)
        return Response(serializer.data)

@api_view(['GET', ])
def get_students_name(request):
    try:
        students = student.objects.order_by('name')

    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentSerializer(students,many=True)
        return Response(serializer.data)

@api_view(['GET', ])
def get_students_search_name(request,name):
    try:
        students = student.objects.filter(name__contains = name)

    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentSerializer(students,many=True)
        return Response(serializer.data)