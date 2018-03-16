from django.conf.urls import url
from Loginapp import views


app_name = 'Loginapp'


urlpatterns=[
	url(r'^register/$',views.register, name='register'),
	url(r'^user_login/$',views.user_login,name='user_login'),
]