# The Installation, Execution, and Testing Guide For Project 3


This document shall cover the start to finish process of installing **django**, **python**, and other requirements used to enable this project to run correctly.
This document shall also cover the step-by-step execution of commands to operate and test the project. **NOTE:** This project is only made to run on the Windows 10 Operating system.


# Installation: 

## 1. Installing python

If you do not have python, this requires any version of python greater than 3.7.x
To install python, please navigate to: https://www.python.org/downloads/ and click the yellow button stating "Download Python"
Once the download is finished, run the installer and complete the steps the installer requires. 


## 2. Installing django

press the keys **WINDOWS + R** and type "CMD" into the box that appears and press enter. 

In the terminal interface, type **pip install django** and press enter. 

Answer yes to any prompts that appear, If django is not added to your PATH variable automatically (you will see a warning if it isnt) please follow the steps to add it.

## 3. The project. 

Within the main page of the github repository, click on the green button that says "Code" and download the project as a .ZIP file. 

Decompress the .ZIP file and move the decompressed file to the desktop.


# Execution: 

## 1. Configuration

To ensure that all systems will work correctly, please type the following commands into the open command prompt. 

1. **django-admin --version** (you are looking for a version greater than 4.0)

2. **python --version** (you are looking for a version greater than 3.7.x)


## 2. Booting up the local server.

Within your command prompt, navigate to the Desktop, then to "adb1042_project_3" or whatever you named the project file after downloading it. 

Type the command **dir** to confirm that you are in the correct directory, and that the "manage.py" file is in that directory. 

Type the command **python manage.py runserver** to boot up the server hosting the project. this server can be navigated to via a web browser by visiting **localhost:8000**

Once at localhost:8000, you will be prompted to enter your height in feet and inches, as well as weight.

When you click the "submit" button, it shall calculate your BMI. 



# Testing:

To test that all system checks have been met within the program, a set of 20 tests have been written to validate that the code has been written properly

To test the code, navigate to the adb1042_project_3 directory and type the command **python manage.py test bmi** 

The output should show that 20 tests were found and 20 tests were run with no errors. If there are errors, please open an issue and put the output there. 

