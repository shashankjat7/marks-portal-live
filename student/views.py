from django.shortcuts import render, redirect, get_object_or_404
from .models import student
from .forms import submitMarksForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,'home.html')


def submit_marks(request):

    context = {}
    if request.POST:
        marks_form = submitMarksForm(request.POST)
        if marks_form.is_valid():
            marks_form.save()
            messages.success(request,'SUCCESSFULLY ENTERED MARKS')
            return redirect('/')
        else:
            messages.error(request,'STUDENT WITH SAME ROLL NO ALREADY EXISTS!!!')
            context['marks_form'] = marks_form
    else:
        marks_form = submitMarksForm()
        context['marks_form'] = marks_form

    return render(request,'student/submit_marks.html')

def leaderboard(request):
    context = {}

    if request.POST:
        students = student.objects.filter(name__contains=request.POST.get('name')).order_by('-percentage')
        context['students'] = students
        return render(request,'student/leaderboard.html',context)
    else:
        students = student.objects.order_by('-percentage')
        context['students'] = students
        return render(request, 'student/leaderboard.html', context)

def leaderboard_ascending(request):
    context = {}

    if request.POST:
        students = student.objects.filter(name__contains=request.POST.get('name')).order_by('percentage')
        context['students'] = students
        return render(request,'student/leaderboard.html',context)
    else:
        students = student.objects.order_by('percentage')
        context['students'] = students
        return render(request, 'student/leaderboard.html', context)
