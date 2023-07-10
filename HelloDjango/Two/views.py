from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render

# 分布加载模版文件
from django.template import loader

from Two.models import Student, Grade, User, Order, Grades, Company, Animal


def index(request):
    two_index = loader.get_template('two_index.html')
    context = {
        "student_name": "Sunck"
    }
    result = two_index.render(context=context)
    print(result)
    return HttpResponse(result)


def get_grade(request):
    # 先获取学生，在获取学生所在班级
    student = Student.objects.get(pk=1)
    grade = student.s_grade
    return HttpResponse("Grade %s" % grade.g_name)


def get_students(request):
    # 获取班级里的所有学生
    grade = Grade.objects.get(pk=1)
    students = grade.student_set.all()
    context = {
        'students': students
    }
    return render(request, 'grade_students.html', context=context)


def get_user(request):
    username = "suny"
    password = "123"

    users = User.objects.filter(u_name=username)

    print(users.count())
    if users.count():
        user = users.first()
        print(password)
        print(user.u_passwd)
        if password == user.u_passwd:
            print("登陆成功")
        else:
            print("密码错误")
    else:
        print("用户不存在")

    return HttpResponse("获取成功")


def get_orders(request):
    # orders = Order.objects.filter(o_date__year=2022)
    orders = Order.objects.filter(o_date__month=7)
    for order in orders:
        print(order.o_date)
    return HttpResponse("获取订单成功")


def get_grades(request):
    grades = Grades.objects.filter(students__s_name='q3')
    for grade in grades:
        print(grade.g_name)
    return HttpResponse('获取成功')


def get_company(request):
    # companies = Company.objects.filter(c_boy_num__gt=F('c_girl_num'))
    # companies = Company.objects.filter(c_boy_num__gt=F('c_girl_num')-15)
    companies = Company.objects.filter(Q(c_boy_num__gt=1) & Q(c_girl_num__gt=10))
    for company in companies:
        print(company.c_name)
    return HttpResponse('获取成功')


def get_animal(request):
    # animals = Animal.objects.all()
    # animals = Animal.am.all()   # am = models.Manager() 模型中将隐性属性声明称线形属性后， 需要用显性属性调用
    animals = Animal.objects.all()
    for animal in animals:
        print(animal.a_name)
    # a = Animal.objects.create_animal()
    # a.save()
    return HttpResponse('获取成功')
