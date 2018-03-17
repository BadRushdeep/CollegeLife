from django.shortcuts import render
from Loginapp.forms import UserProfileInfoForm, UserForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login,logout,authenticate






# Create your views here.
def index(request):
	return render(request,'Loginapp/index.html')

@login_required
def special(request):
	return render(request,'Loginapp/dashboard.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def register(request):

	registered = False

	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(request.POST,request.FILES)

		if user_form.is_valid() and profile_form.is_valid() :

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.profile_pic = profile_form.cleaned_data['profile_pic']
			profile.doc_image = profile_form.cleaned_data['doc_image']
			profile.save()

			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request,'Loginapp/registeration.html',
		                   {'user_form':user_form,
		                    'profile_form':profile_form,
		                    'registered':registered,
							})



def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/special/')

			else:
				return HttpResponse("Account Not Active")

		else:
			print("Someone tried to login and failed!")
			return HttpResponse("Invalid login details")

	else:
		return render(request,'Loginapp/login.html')
