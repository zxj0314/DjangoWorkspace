from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^one/', views.appone),
    url(r'^addstudent/', views.addstudent),
    url(r'^getstudents/', views.getstudents),
    url(r'update/',views.update),
    url(r'^deletestudent/',views.delete),
    url(r'^addpersons/',views.addpersons),
    url(r'^getpersons/',views.getpersons),
    url(r'^addperson/',views.addperson),
    url(r'^getperson/',views.getperson)
]
