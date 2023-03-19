import pytest
from io import StringIO
from ADB1042_Project_2_BMI import BMI_AVG as BMI
from ADB1042_Project_2_BMI import main as Calc

# weak Nx1 tests for catching boundary shift in BMI_AVG

def testUnderBoundaryUpperOn():
    assert BMI(18.4) == "You Are Under Weight." #ON

def testUnderBoundaryUpperOff():
    assert BMI(18.5)  == "You Are A Normal Weight."  #OFF


    
    
def testNormalBoundaryLowerOff(): 
    assert BMI(18.4) == "You Are Under Weight." #OFF

    
def testNormalBoundaryLowerOn():
    assert BMI(18.5)  == "You Are A Normal Weight."  #ON

def testNormalBoundaryInterior():
    assert BMI(22) == "You Are A Normal Weight." #INTERIOR


def testNormalBoundaryUpperON():
    assert BMI(24.9) == "You Are A Normal Weight." #ON

def testNormalBoundaryUpperOFF():
    assert BMI(25) == "You Are Over Weight."#OFF






def testOverBoundaryLowerOff():
     assert BMI(24.9) == "You Are A Normal Weight." #OFF

def testOverBoundaryLowerOn():
     assert BMI(25) == "You Are Over Weight." #ON

def testOverBoundaryInterior():
    assert BMI(27) == "You Are Over Weight." #INTERIOR

def testOverBoundaryUpperOn():
    assert BMI(29.9) == "You Are Over Weight." #ON

def testOverBoundaryUpperOff():
    assert BMI(30) == "You Are Obese." #OFF






def testOveseBoundaryLowerOff():
    assert BMI(29.9) == "You Are Over Weight." #OFF
    
def testObeseBoundaryLowerOn():
    assert BMI(30) == "You Are Obese." #ON
    


#tests the math behind calculating the BMI given weight, feet, and inches.
    
def testBMIMathCalculations(monkeypatch):
    insertOne = StringIO('160\n5\n8\n')    
    monkeypatch.setattr('sys.stdin', insertOne)
    

    assert Calc() == 24.9

#tests if invalid inputs are flagged and handled.
        
def testBMIMathCalculationExceptionHandling(monkeypatch):
    with pytest.raises(Exception) as e_info:
        insertOne = StringIO('apple\napple\napple\n')
        monkeypatch.setattr('sys.stdin',insertOne)
        assert Calc() == 24.9
        


    
    


    
