from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.views.generic import RedirectView
from . import views


urlpatterns=[
	path('', views.index, name='index'),
	path('upload', views.upload, name='upload'),
	path('display', views.display, name='display'),
	path('get_emails/', views.get_emails, name='get_emails'),
	path('predisplay/<int:fileid>/', views.predisplay, name='predisplay'),
	path('nextpara/<int:fileid>/', views.nextpara, name='nextpara'),
	path('save_data_back', views.save_data_back, name='save_data_back'),
	path('savecall', views.savecall, name='savecall'),
]