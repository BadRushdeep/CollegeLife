from django import forms
from django.contrib.auth.models import User
from Loginapp.models import UserProfileInfo,College

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	class Meta():
		model = User
		fields = ('username', 'email', 'password')


class CollegeForm(forms.ModelForm):
	college = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'College'}))
	class Meta():
		model = College
		fields = '__all__'

class UserProfileInfoForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
	mob_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile No'}))
	#college = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'College Name'}))
	dob = forms.DateField(widget=forms.SelectDateWidget(years=[y for y in range(1930,2050)],attrs={'class':'form-control form-inline inline inlinef'}))
	doc_image = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Document Image'}))
	profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Profile Pic'}))
	class Meta():
		model= UserProfileInfo
		fields = ('first_name','last_name','mob_no','doc_image','college','dob','profile_pic')
