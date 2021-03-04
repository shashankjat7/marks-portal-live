from rest_framework import serializers
from student.models import student

class studentSerializer(serializers.ModelSerializer):

    class Meta:
        model = student
        fields = ['roll_no','name','marks_maths','marks_physics','marks_chemistry',
                  'total','percentage']



