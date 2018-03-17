from django.conf.urls import url
from . import views
#from . views import Upvote
app_name='Issues'
urlpatterns=[
	url(r'^$',views.problem,name='problem'),
]
