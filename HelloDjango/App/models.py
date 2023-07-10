from django.db import models


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)


class Person(models.Model):
    p_name = models.CharField(max_length=32)
    p_age = models.IntegerField(default=1)
    # False代表男，True代表女
    p_sex = models.BooleanField(default=True)

    @classmethod
    def create(cls, p_name, p_age=3, p_sex=True):
        return cls(p_name=p_name, p_age=p_age, p_sex=p_sex)

    class Meta:
        db_table = 'People'
