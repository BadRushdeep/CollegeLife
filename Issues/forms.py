from django import forms
from Issues.models import Problem

class ProblemForm(forms.ModelForm):
	class Meta():
		model = Problem
		fields = ('prob_stat',)