from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from User.models import Student
import random

def index(request):
    return HttpResponse("aaads")


def add_student(request):
    student = Student()
    student.s_name = 'Jerry%d' % random.randrange(100)
    student.save()
    return HttpResponse("add%s" % student.s_name)


def get_students(request):
    students = Student.objects.all()
    for student in students:
        print(student.s_name)

    context = {
        'hobby': 'liu',
        'students': students
    }
    return render(request, 'student_list.html.html', context)


def updatestudents(request):
    student = Student.objects.get(pk=2)
    student.s_name = "Jack"
    student.save()
    return HttpResponse('nice')


def deletestudents(request):
    student = Student.objects.get(pk=3)
    student.delete()
    return HttpResponse('delete')