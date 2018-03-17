from django.shortcuts import render
from .forms import ProblemForm
from .models import Problem
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from Loginapp.models import UserProfileInfo, College
from django.contrib.auth.models import User



# Create your views here.
@login_required
def problem(request):
	form = ProblemForm()
	
	prob = Problem()
	if request.method == 'POST':
		form = ProblemForm(request.POST)
		
		
		prob.college=UserProfileInfo.objects.filter(user=request.user)[0].college
		print(prob.college)
		prob.save()
		# form.college = UserProfileInfo.objects.filter(user=request.user)[0].college
		# form.prob_stats = request.POST.prob_stats

		# print(form)
		# prob.college = request.user.College.college
		#print(prob.creator)
		#print(prob.college)

		
		
		if form .is_valid():
			form.save()
			return HttpResponse("Problem Solved")
		else:
			return HttpResponse("Error in form")
	return render(request,'Issues/Problem.html',{'form':form,})


