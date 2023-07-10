import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student, Person


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


def addpersons(request):
    for i in range(1, 100):
        person = Person()
        person.p_name = 'Tom%s' % i
        person.p_age = i
        person.p_sex = i % 2
        person.save()
    return HttpResponse("Add Person success.")


def getpersons(request):
    # persons = Person.objects.filter(p_age__lt=60).filter(p_age__gt=30)
    # 排序
    # persons = Person.objects.all().order_by('-id')  # 根据ID排序，-id代表倒序
    persons = Person.objects.all().order_by('p_age')  # 根据

    person_values = Person.objects.values()  # 返回字典数据的列表
    print(type(person_values))
    print(person_values)
    for person_value in person_values:
        print(person_value)

    person_value_list = Person.objects.values_list()  # id+数据的元组数据列表
    print("*" * 50)
    print(type(person_value_list))
    print(person_value_list)
    context = {
        "persons": persons
    }
    return render(request, 'get_persons.html', context=context)


def addperson(request):
    # person = Person.objects.create(p_name='Jack', p_age=38, p_sex=True)
    # print(person.p_name)
    person = Person.create("Jacny")
    person.save()
    return HttpResponse("add success")


def getperson(request):
    person = Person.objects.get(p_age=100)
    return HttpResponse('获取成功')
