from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    # path('student_view_attendance',views.student_view_attendance, name="student_view_attendance")
    # path('', views.home, name ="home"),
    # path('signup', views.signup, name ="signup"),
    # path('signin', views.signin, name ="signin"),
    # path('logout', views.logout, name ="logout"),
]