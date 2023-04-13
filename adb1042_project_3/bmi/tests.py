from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bmi.views import calculate, calcBMI, BMI_AVG
from bmi.forms import BMIForm


class TestURLs(SimpleTestCase):     

	def test_bmi_homepage_is_resolved(self):   #check if homepage is routed to correctly
		url = reverse('BMI-Calculator')
		self.assertEquals(resolve(url).func,calculate)


class TestVIEWS(SimpleTestCase):  #testing bmi calculation math with known variables
	def test_bmi_math(self):
		assert calcBMI(5,8,160)== 24.9

	def test_bmi_avg_Under_U_ON_boundary(self):   #testing the boundaries of BMI_AVG
		assert BMI_AVG(18.4)=="You Are Under Weight."
	def test_bmi_avg_Under_U_OFF__boundary(self):
		assert BMI_AVG(18.5)=="You Are A Normal Weight."
	def test_bmi_avg_Normal_L_OFF_boundary(self):
		assert BMI_AVG(18.4)=="You Are Under Weight."
	def test_bmi_avg_Normal_L_ON_boundary(self):
		assert BMI_AVG(18.5)=="You Are A Normal Weight."
	def test_bmi_avg_Normal_INT_boundary(self):
		assert BMI_AVG(22.0)=="You Are A Normal Weight."
	def test_bmi_avg_Normal_U_ON_boundary(self):
		assert BMI_AVG(24.9)=="You Are A Normal Weight."
	def test_bmi_avg_Normal_U_OFF_boundary(self):
		assert BMI_AVG(25)=="You Are Over Weight."
	def test_bmi_avg_Over_L_OFF_boundary(self):
		assert BMI_AVG(24.9)=="You Are A Normal Weight."
	def test_bmi_avg_Over_L_ON_boundary(self):
		assert BMI_AVG(25)=="You Are Over Weight."
	def test_bmi_avg_Over_INT_boundary(self):
		assert BMI_AVG(28)=="You Are Over Weight."
	def test_bmi_avg_Over_U_ON_boundary(self):
		assert BMI_AVG(29.9)=="You Are Over Weight."
	def test_bmi_avg_Over_U_OFF_boundary(self):
		assert BMI_AVG(30)=="You Are Obese."
	def test_bmi_avg_Obese_L_OFF_boundary(self):
		assert BMI_AVG(29.9)=="You Are Over Weight."
	def test_bmi_avg_Obese_L_ON_boundary(self):
		assert BMI_AVG(30)=="You Are Obese."


		#  "You Are Under Weight."     "You Are A Normal Weight." 
		#  "You Are Over Weight."      "You Are Obese."



class TestFORMS(SimpleTestCase):

	def test_form_with_valid_arguments(self): #testing if the form assertions are held with valid data
		form = BMIForm(data={
			'feet':5,
			'inches':8,
			'weight':160
			})
		self.assertTrue(form.is_valid())


	def test_form_with_no_data(self):   #testing if the form assertions return false with no data (data is required for the form to return successfully)
		form = BMIForm(data={})
		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors),3)

	def test_form_with_invalid_type_data(self): #testing if the form assertions return false with wrong type of data (all fields require integers)
		form = BMIForm(data={
			'feet':'apple',
			'inches':'oranges',
			'weight':'bananas'
			})
		self.assertFalse(form.is_valid())

	def test_form_with_out_of_range_data(self): #testing if the form assertions prevent improper math from occuring (prevents divide by zero errors and from weight being zero)
		form = BMIForm(data={
			'feet': 0,
			'inches':-12,
			'weight':0
			})
		self.assertFalse(form.is_valid())



		#TOTAL NUMBER OF TESTS: 20










