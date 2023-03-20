# Installation and execution guide for BMI Calculator and PyTest.  
This document covers the installation of python, PyTest, and how to execute both ADB1042_Project_2_BMI.py and test_ADB1042_Project_2_BMI.py, which will hereby be respectively referred to as "Main.py" and "Test.py."  Note, this install guide is for Windows 10 only, and has only been tested on such.

## Python  

### Windows OS  

To install Python onto your Windows machine: 

1. navigate to: https://www.python.org/downloads/ 
2. click "Download Python" (the most current version number will be on the button)
3. Once the file has completed downloading, open the installer file.
4. within the installer window, click "Install now."
5. follow the rest of the instructions to complete installing python.


## Pytest
**To install pytest on windows, you must have already installed python on windows.**  

1. open command prompt.
2. type *python --version* to verify python is installed. 
3. type *pip install pytest* and begin downloading. 
4. after the download is finished, type *pytest* and see if anything appears.
5. If you see "pytest is not a recognized program" you must add the directory pytest was downloaded into to your PATH variable.
6. (optional) If you need to add the pytest folder to your path variable, visit: https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/ to learn how.
7. (optional) Once pytest has been added to path, close and re-open your command prompt to refresh the environment variables.


## Install Main.py and Test.py

1. Download the repository from github: https://github.com/adb1042/SW-QA_Projects.git
2. Decompress the ZIP file.
3. Navigate through command prompt to the **Project_2** folder.  
4. run *python ADB1042_Project_2_BMI*
5. Complete the steps to calculate your BMI. 
6. run *pytest* to view the current boundary shift issue.
7. to view the code in both Main.py and Test.py, press **Windows + R**
8. inside the dialog box that appears, type *idle*
9. when idle opens, press **CTRL + O**
10. navigate to the **Project_2** folder, and select the file you wish to view.

