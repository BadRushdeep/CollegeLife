from django.conf.urls import url
from . import views
app_name='Issues'
urlpatterns=[
	url(r'^$',views.problem,name='problem'),
]
