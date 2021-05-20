# COVIDGUI
Dependecies to be installed:<br />
Python<br/>
Tkinter<br/>
Requests<br/>
Step 1: Select Version of Python to Install
The installation procedure involves downloading the official Python .exe installer and running it on your system.

The version you need depends on what you want to do in Python. For example, if you are working on a project coded in Python version 2.6, you probably need that version. If you are starting a project from scratch, you have the freedom to choose.

If you are learning to code in Python, we recommend you download both the latest version of Python 2 and 3. Working with Python 2 enables you to work on older projects or test new projects for backward compatibility.
Open your web browser and navigate to the Downloads for Windows section of the official Python website.
Search for your desired version of Python. At the time of publishing this article, the latest Python 3 release is version 3.7.3, while the latest Python 2 release is version 2.7.16.
Select a link to download either the Windows x86-64 executable installer or Windows x86 executable installer. The download is approximately 25MB.<br />
Step 2: Download Python Executable Installer
Open your web browser and navigate to the Downloads for Windows section of the official Python website.
Search for your desired version of Python. At the time of publishing this article, the latest Python 3 release is version 3.7.3, while the latest Python 2 release is version 2.7.16.
Select a link to download either the Windows x86-64 executable installer or Windows x86 executable installer. The download is approximately 25MB
![alt text](https://phoenixnap.com/kb/wp-content/uploads/2021/04/python-for-windows.png)<br />
Step 3: Run Executable Installer
1. Run the Python Installer once downloaded. (In this example, we have downloaded Python 3.7.3.)

2. Make sure you select the Install launcher for all users and Add Python 3.7 to PATH checkboxes. The latter places the interpreter in the execution path. For older versions of Python that do not support the Add Python to Path checkbox, see Step 6.

3. Select Install Now – the recommended installation options.
![alt text](https://phoenixnap.com/kb/wp-content/uploads/2021/04/python-setup.png)<br />
For all recent versions of Python, the recommended installation options include Pip and IDLE. Older versions might not include such additional features.

4. The next dialog will prompt you to select whether to Disable path length limit. Choosing this option will allow Python to bypass the 260-character MAX_PATH limit. Effectively, it will enable Python to use long path names.
![alt text](https://phoenixnap.com/kb/wp-content/uploads/2021/04/python-setup-completed.png)<br />
The Disable path length limit option will not affect any other system settings. Turning it on will resolve potential name length issues that may arise with Python projects developed in Linux.

Step 4: Verify Python Was Installed On Windows  
Navigate to the directory in which Python was installed on the system. In our case, it is C:UsersUsernameAppDataLocalProgramsPythonPython37 since we have installed the latest version.
Double-click python.exe.
The output should be similar to what you can see below:
![alt text](https://phoenixnap.com/kb/wp-content/uploads/2021/04/verify-python-install-1.png)<br />
Step 5: Verify Pip Was Installed
If you opted to install an older version of Python, it is possible that it did not come with Pip preinstalled. Pip is a powerful package management system for Python software packages. Thus, make sure that you have it installed.

We recommend using Pip for most Python packages, especially when working in virtual environments.

To verify whether Pip was installed:

Open the Start menu and type “cmd.”
Select the Command Prompt application.
Enter pip -V in the console. If Pip was installed successfully, you should see the following output:
![alt text](https://phoenixnap.com/kb/wp-content/uploads/2021/04/verify-pip.png)<br />

Pip has not been installed yet if you get the following output:
’pip’ is not recognized as an internal or external command,
Operable program or batch file.
If your version of Python is missing Pip, see our article How to Install Pip to Manage Python Packages on Windows.If your version of Python is missing Pip, see our article How to Install Pip to Manage Python Packages on Windows.
https://phoenixnap.com/kb/install-pip-windows

Download the dependencies with the terminal or cmd:
1.Install tk
![alt text](https://github.com/aman22032007/COVIDGUI/blob/main/Screenshot%20from%202021-05-20%2018-54-25.png?raw=true)<br />
2.Install requests
![alt text](https://github.com/aman22032007/COVIDGUI/blob/main/Screenshot%20from%202021-05-20%2018-58-53.png?raw=true)<br />

Then download the zip folder 
To excute:
1.Cd to the folder:
![alt text](https://github.com/aman22032007/COVIDGUI/blob/main/Screenshot%20from%202021-05-20%2018-59-54.png?raw=true)<br />
2.Run the file:
![alt text](https://github.com/aman22032007/COVIDGUI/blob/main/Screenshot%20from%202021-05-20%2018-59-42.png?raw=true)<br />
3.Woila you have your app running.
![alt text](https://github.com/aman22032007/COVIDGUI/blob/main/2021-05-20%2019-12-44.gif?raw=true)<br />
