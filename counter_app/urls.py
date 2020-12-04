from django.urls import path
from . import views

urlpatterns = [
	path('', views.some_function),
	path('process_form', views.process_form),
    path('destroy_session', views.destroy_session),
]
