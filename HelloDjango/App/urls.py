from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^one/', views.appone),
    url(r'^addstudent/', views.addstudent),
    url(r'^getstudents/', views.getstudents),
    url(r'update/',views.update),
    url(r'^deletestudent/',views.delete)
]
