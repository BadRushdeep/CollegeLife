from django.conf.urls import url
from Loginapp import views


app_name = 'Loginapp'


urlpatterns=[
	url(r'^register/$',views.register, name='register'),
	url(r'^user_login/$',views.user_login,name='user_login'),
	url(r'^$',views.account,name='account'),
	url(r'^college/$',views.college,name='college')

]
