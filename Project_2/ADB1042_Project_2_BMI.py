#The purpose of this program is to calculate the Body Mass Index (BMI) of
#The user, given their height and weight in either standard or metric systems.
#written by Andrew Brewer -- NETID: adb1042

def BMI_AVG(Index):     #Function that takes the BMI and tells you where you are on the spectrum
    if (Index < 18.5):
        print("You are Under Weight.")
    if(Index >= 18.5 and Index <=24.9):
        print("You are a Normal Weight.")
    if(Index >= 25 and Index <=29.9):
        print("You are Over Weight.")
    if(Index >=30):
        print("You are Obese.")



print("Welcome to the Body Mass Index Calculator!")
        
print("Please enter your weight pounds.\n")
Weight=0.45* float(input("Lbs:"))  #grabs the body weight in Pounds and converts to Kilograms
print("\nPlease enter your height in feet and then inches.\n")
Feet = int(input("Ft:")) #Grabs the height in Feet
Inches =int(input("In:")) #Grabs the height in Inches
Height =float((0.025*((Feet * 12) + Inches))**2) #converts feet to inches,converts to meters, and squares the result.
BMI = Weight/Height
BMI = round(BMI,1) #rounds the BMI to 1 decimal place
print("Your BMI is:")
print(BMI)  
BMI_AVG(BMI)







def DEBUG_PrintVars():  #debug only, used strictly to print variables to test if the math is done properly.
    print("Height: ")
    print(Height)
    print("Weight: ")
    print(Weight)
    print("Feet: ")
    print(Feet)
    print("Inches: ")
    print(Inches)
    print("BMI")
    print(BMI)



