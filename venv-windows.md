# Running Virtualized Python Environments in Windows

## Steps
1. Ensure you have Python installed
1. Make sure your Python installation includes pip and virtualenv. If not, install them
1. Run the following command:
    ````python -m venv ENV3````<br/>
1. Run the activation script. On windows, your activation script will exist inside `BASEPATH\ENV3\Scripts`.
1. If everything worked correctly, you should now see a `(ENV3)` preceeding the text you would normally see in your terminal.
1. To exit the virtual environment, simply type `deactivate`