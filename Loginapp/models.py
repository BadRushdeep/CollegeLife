from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class College(models.Model):
	 college = models.CharField(max_length=200)

	 def __str__(self):
	 	return self.college

class UserProfileInfo(models.Model):

	#creating one to one relation with the admin model
	user=models.OneToOneField(User,on_delete=models.CASCADE )
	first_name = models.CharField(max_length=60, default='firstname', blank=False)
	last_name = models.CharField(max_length=60, default='lastname', blank=False)
	doc_image = models.ImageField(upload_to='documents', default='profile_pics/sumit.jpg', blank=False)
	college = models.ForeignKey(College, on_delete=models.CASCADE)
	mob_no = models.CharField(max_length=13, default='67567574', blank=False)
	dob = models.DateField( default=date.today, blank=False)




	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics' ,blank=True)

	def __str__(self):
		
		return self.user.username

