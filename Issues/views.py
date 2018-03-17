from django.shortcuts import render
from .forms import ProblemForm,UpvoteForm
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
		if form .is_valid():
			prob.college=UserProfileInfo.objects.filter(user=request.user)[0].college
			data = form.cleaned_data

			prob.prob_stat =data['prob_stat']
			prob.save()


			print(Problem.college)
			return HttpResponseRedirect("../../special")
		else:
			return HttpResponse("Error in form")
	return render(request,'Issues/Problem.html',{'form':form,})

def display(request):
	issue_list = Problem.objects.order_by('created')
	ucol = UserProfileInfo.objects.filter(user=request.user)[0].college
	return render(request,'Issues/display.html',{'display':issue_list,'college':ucol})
