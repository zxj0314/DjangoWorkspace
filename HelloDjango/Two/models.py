from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=16)


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


class User(models.Model):
    u_name = models.CharField(max_length=32)
    u_passwd = models.CharField(max_length=256)


class Order(models.Model):
    o_num = models.CharField(max_length=16, unique=True)
    o_date = models.DateTimeField(auto_now_add=True)


class Grades(models.Model):
    g_name = models.CharField(max_length=16)


class Students(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grades, on_delete=models.CASCADE)


class Company(models.Model):
    c_name = models.CharField(max_length=32)
    c_girl_num = models.IntegerField(default=1)
    c_boy_num = models.IntegerField(default=1)


class AnimalManager(models.Manager):
    # 重写get_queryset()方法
    def get_queryset(self):
        return super(AnimalManager, self).get_queryset().filter(is_delete=False)

    # 模型内创建方法
    def create_animal(self, a_name='checken'):
        a = self.model()
        a.a_name = a_name
        return a


class Animal(models.Model):
    a_name = models.CharField(max_length=32)
    is_delete = models.IntegerField(default=False)
    # objects = models.Manager()  # 查询调用时，需要使用objects,不是使用object
    objects = AnimalManager()  # 自定义类，重写方法
