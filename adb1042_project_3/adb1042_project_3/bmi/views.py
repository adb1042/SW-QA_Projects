from django.shortcuts import render
from django.http import HttpResponse
from .forms import BMIForm
from django.contrib import messages
def calcBMI(feet,inches,weight):
	w = weight * 0.45
	h = ((0.025*((feet * 12) + inches))**2)
	B = w/h
	B = round(B,1)
	return B

def BMI_AVG(B):
	if(B < 18.5):
		x = "You Are Under Weight."
		return(x)
	if(B >=18.5 and B<=24.9):
		x="You Are A Normal Weight."
		return(x)
	if(B>=25 and B <= 29.9):
		x="You Are Over Weight."
		return(x)
	if(B>=30):
		x = "You Are Obese."
		return(x)
		









# Create your views here.
def calculate(request):
	BMI = 0
	if request.method == 'POST':
		form=BMIForm(request.POST)
		if form.is_valid():
			feet = form.cleaned_data.get('feet')
			inches = form.cleaned_data.get('inches')
			weight = form.cleaned_data.get('weight')
			BMI = calcBMI(feet,inches,weight)
			messages.success(request, f'Your BMI is:{BMI}')
			getThiccStatus = BMI_AVG(BMI)
			messages.success(request, f'{getThiccStatus}')



	else:
		form = BMIForm()

	return render(request, 'bmi/calculate.html',{'form':form})
