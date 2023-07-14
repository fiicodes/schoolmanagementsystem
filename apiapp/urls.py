from django.urls import path,include
from django import urls
from apiapp import views


urlpatterns = [
  
   
    path("teacherlist/",views.teacherlist,name="teacherlist"),

    path("courselist/",views.courselist,name="courselist"),
    path("courselist/<int:id>",views.coursedetail,name="coursedetail"),
    path("addcourseapi/",views.addcourseapi,name="addcourseapi")
]
