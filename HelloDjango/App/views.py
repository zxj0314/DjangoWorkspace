import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student


def hello(request):
    return HttpResponse("Hello Django.")


def haha(request):
    return HttpResponse("<h1>哈哈</h1>")


def index(request):
    return render(request, 'index.html')  # App下的templates模板文件


def home(request):
    return render(request, 'home.html')  # 项目内创建的模板文件，但要在settings.py的TEMPLATES中的DIRS中注册templates模版相对路径


def appone(request):
    return HttpResponse("<h1>Hello App One </h1>")


def addstudent(request):
    student = Student()
    student.s_name = 'Jerry%d' % random.randint(1, 100)
    student.s_age = random.randint(1, 100)
    student.save()
    return HttpResponse("Add success")


def getstudents(request):
    students = Student.objects.all()
    # print(students)
    # for student in students:
    #     print(student.s_name)
    # html 模板传递参数,传递字典参数,在HTML中使用{{hobby}}接收hobby传递的参数
    context = {
        'hobby': 'Play Games',
        'eat': 'meat',
        'students': students
    }
    # return HttpResponse("get students list")
    return render(request, 'student_list.html', context=context)


def update(request):
    student = Student.objects.get(pk=5)
    student.s_name = 'Jack merry'
    student.save()
    return HttpResponse("Update Student name Success.")


def delete(request):
    student = Student.objects.get(pk=6)
    student.delete()
    return HttpResponse("delete sutdent 3 Success")
