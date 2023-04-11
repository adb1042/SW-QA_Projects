from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from django.contrib import messages
def calcBMI(feet,inches,weight):
	w = weight * 0.45
	h = ((0.025*((feet * 12) + inches))**2)
	B = w/h
	B = round(B,1)
	return B



# Create your views here.
def calculate(request):
	BMI = 0
	if request.method == 'POST':
		form=InputForm(request.POST)
		if form.is_valid():
			feet = form.cleaned_data.get('feet')
			inches = form.cleaned_data.get('inches')
			weight = form.cleaned_data.get('weight')
			messages.success(request, f'Feet:{feet}')
			messages.success(request, f'Inches:{inches}')
			messages.success(request, f'Weight:{weight}')
			BMI = calcBMI(feet,inches,weight)
			messages.success(request, f'Your BMI is:{BMI}')


	else:
		form = InputForm()

	return render(request, 'bmi/calculate.html',{'form':form})
