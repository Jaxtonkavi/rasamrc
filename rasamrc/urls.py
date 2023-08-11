"""rasamrc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Main_page'),
    re_path(r'^who_we_are/$', views.who_we_are, name='who_we_are'),
    re_path(r'^ceo_message/$', views.ceo_msg, name='ceo_message'),
    re_path(r'^coo_message/$', views.coo_msg, name='coo_message'),
    re_path(r'^ocv/$', views.ocv, name='ocv'),
    re_path(r'^mission_vision/$', views.Mission_vision, name='mission_vision'),
    re_path(r'^testimonials/$', views.Testimonials, name='Testimonials'),
    re_path(r'^apply_job/$', views.apply_job, name='apply_job'),
    re_path(r'^employer_portal/$', views.employer_portal, name='employer_portal'),
    re_path(r'^career/$', views.career, name='career'),
    re_path(r'^HR_career/$', views.HR_career, name='HR_career'),
    re_path(r'^Education/$', views.Education, name='Education'),
    re_path(r'^software/$', views.software, name='software'),
    re_path(r'^operations/$', views.operations, name='operations'),
    re_path(r'^BTD/$', views.BTD, name='BTD'),
]
