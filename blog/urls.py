from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    
	url(r'^$', views.post_list, name='post_list'),
   
]
