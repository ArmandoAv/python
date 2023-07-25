# python

In this project some aspects of programming in Python will be seen, the programs executed are in a Windows environment.

For the creation and execution of the files were made in Visual Studio Code, this software is in the following link

https://code.visualstudio.com/

When installing Python, the following path must be added to the environment variables in Path

C:\....\Programs\Python\Python38\

The path will change according to where Python is installed.

That will recognize the python command from a cmd terminal or from the Visual Studio Code terminal.

In addition, a virtual Python environment was created so that batch files can be executed without having to change the paths.

In the folder that they have assigned for their files, the following command must be executed from a terminal

python -m venv environment_name

This command has to create the next folders

environment_name
   Include
   Lib
   Scripts

And the next file

pyvenv.cfg

To activate the virtual environment, the following command must be executed

.\enviroment_name\Scripts\activate.bat

To deactivate the virtual environment, the following command must be executed

.\enviroment_name\Scripts\deactivate.bat

