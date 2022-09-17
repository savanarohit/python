"""
Step 1: Download the Python Installer binaries
Open the official Python website in your web browser. Navigate to the Downloads tab for Windows.
Choose the latest Python 3 release. In our example, we choose the latest Python 3.7.3 version.
Click on the link to download Windows x86 executable installer if you are using a 32-bit installer. 
In case your Windows installation is a 64-bit system, then download Windows x86-64 executable installer.

Step 2: Run the Executable Installer
Once the installer is downloaded, run the Python installer.
Check the Install launcher for all users check box. Further, 
you may check the Add Python 3.7 to path check box to include the interpreter in the execution path.

Select Customize installation. Choose the optional features by checking the following check boxes:

Documentation
pip
tcl/tk and IDLE (to install tkinter and IDLE)
Python test suite (to install the standard library test suite of Python)
Install the global launcher for `.py` files. This makes it easier to start Python
Install for all users.

Click Next.8. This takes you to Advanced Options available while installing Python. Here, select the Install for all users and Add Python to environment variables check boxes. Optionally, you can select the Associate files with Python, Create shortcuts for installed applications and other advanced options. Make note of the python installation directory displayed in this step. You would need it for the next step. After selecting the Advanced options, click Install to start installation.


10. Once the installation is over, you will see a Python Setup Successful window.


Step 3: Add Python to environmental variables
The last (optional) step in the installation process is to add Python Path to the System Environment variables. This step is done to access Python through the command line. In case you have added Python to environment variables while setting the Advanced options during the installation procedure, you can avoid this step. Else, this step is done manually as follows. In the Start menu, search for “advanced system settings”. Select “View advanced system settings”. In the “System Properties” window, click on the “Advanced” tab and then click on the “Environment Variables” button. Locate the Python installation directory on your system. If you followed the steps exactly as above, python will be installed in below locations:

C:\Program Files (x86)\Python37-32: for 32-bit installation
C:\Program Files\Python37-32: for 64-bit installation
The folder name may be different from “Python37-32” if you installed a different version. Look for a folder whose name starts with Python. 

Step 4: Verify the Python Installation
You have now successfully installed Python 3.7.3 on Windows 10. You can verify if the Python installation is successful either through the command line or through the IDLE app that gets installed along with the installation. Search for the command prompt and type “python”. You can see that Python 3.7.3 is successfully installed.

An alternate way to reach python is to search for “Python” in the start menu and clicking on IDLE (Python 3.7 64-bit). You can start coding in Python using the Integrated Development Environment(IDLE).



"""
