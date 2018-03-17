from django import forms
from Issues.models import Problem

class ProblemForm(forms.ModelForm):
	prob_stat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Problem'}))
	class Meta():
		model = Problem
		fields=('prob_stat',)

class UpvoteForm(forms.ModelForm):
	class Meta():
		model = Problem
		fields = ('booltrue',)
