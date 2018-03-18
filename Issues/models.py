from django.db import models
from Loginapp.models import College, UserProfileInfo
from django.contrib.auth.models import User
from updown.fields import RatingField
from datetime import date

# Create your models here.
class Problem(models.Model):
	prob_stat = models.TextField()
	created = models.DateField(default=date.today)

	college = models.ForeignKey(College, related_name='collegename' , null=True,blank=True,on_delete = models.CASCADE)
	rating = RatingField(can_change_vote=True,blank=True,null=True)
	count =models.IntegerField(blank=True, null=True)
	booltrue = models.BooleanField(default=False)

	def __str__(self):
		return self.prob_stat
