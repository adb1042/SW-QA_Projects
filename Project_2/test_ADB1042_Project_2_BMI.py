from io import StringIO
from ADB1042_Project_2_BMI import BMI_AVG as BMI
from ADB1042_Project_2_BMI import Calculate as Calc

def testUnderBoundary():
    assert BMI(18.4) == "You Are Under Weight."

    
def testNormalBoundaryLower():
    assert BMI(18.5)  == "You Are A Normal Weight."

def testNormalBoundaryUpper():
    assert BMI(24.9) == "You Are A Normal Weight."

def testOverBoundaryLower():
    assert BMI(25) == "You Are Over Weight."

def testOverBoundaryUpper():
    assert BMI(29.9) == "You Are Over Weight."

def testObeseBoundary():
    assert BMI(30) == "You Are Obese."
    



    
def testCalcMath(monkeypatch):
    insertOne = StringIO('160\n5\n8\n')
    monkeypatch.setattr('sys.stdin', insertOne)
    

    assert Calc() == 24.9
    
    


    
