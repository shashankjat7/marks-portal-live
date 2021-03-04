from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('submit_marks/',views.submit_marks_view,name='submit_marks'),
    path('get_students/',views.get_students,name='get_students'),
    path('get_students_reverse/',views.get_students_reverse,name='get_students_reverse'),
    path('get_students_roll/',views.get_students_roll,name='get_students_roll'),
    path('get_students_name/',views.get_students_name,name='get_students_name'),
    path('get_students_search_name/<name>',views.get_students_search_name,name='get_students_search_name'),

]