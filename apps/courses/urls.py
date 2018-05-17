from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'destroy/(\d+)', views.destroy),
	url(r'courses', views.index),
	url(r'^delete_process', views.delete_process),
	url(r'^submit_course', views.submit_course),
	url(r'^', views.index),
]
