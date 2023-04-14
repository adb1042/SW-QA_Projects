from django import forms

# creating a form
class BMIForm(forms.Form):

	feet = forms.IntegerField(min_value=1,  help_text="If you are 6'2\". You will enter your height as Feet:6 Inches: 2")
	inches = forms.IntegerField(min_value=-11)
	weight = forms.IntegerField(min_value=1)
	
