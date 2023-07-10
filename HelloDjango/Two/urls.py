from django.conf.urls import url

from Two import views

urlpatterns= [
    url(r'^indexs/',views.index),
    url(r'^get_grade/',views.get_grade),
    url(r'^getstudents/',views.get_students),
    url(r'^getuser/',views.get_user),
    url(r'get_orders/',views.get_orders),
    url(r'get_grades/',views.get_grades),
    url(r'getcompany/',views.get_company),
    url(r'^getanimal/',views.get_animal),




]