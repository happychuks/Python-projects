# Python Package
## Installing a Python Package using Modularized Code
You can put your code into the python_package folder in your local computer or a virtual environment (see bottom page for more info in virtual env). Inside the python_package folder, you'll need to create a few folders and files:
* a setup.py file, which is required in order to use pip install
* a folder called 'distributions', which is the name of the Python package
* inside the 'distributions' folder, you'll need the Gaussiandistribution.py file, Generaldistribution.py and an __init__.py file.

Once everything is set up, you'll need to open a new terminal and do the following command:
- switch to the python package directory
- run command `pip install .`
  If everything is set up correctly, pip will install the distributions package into the workspace. You can then start the python interpreter from the terminal typing:
`python`
- then within the interpreter,  you can use the distributions package:  
    Test using:
    ```python 
    from distributions import Gaussian, Binomial
    Gaussian(10, 7)
    Binomial(.5, 25)    
    ```
## How to use venv and pip, the commands look something like this:
```python
python3 -m venv environmentname
source environmentname/bin/activate
```
It is advisable to switch to a virtual environment when installing packages that are not directly available on python. 

## Uploading to pypi repository
```bash 
cd <packages directory name>
python setup.py sdist
pip install twine
or python3 -m pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ <package name>

# command to upload to the pypi repository
twine upload dist/*
pip install <package name>
```
## You can install this package from the pypi.org repository using the following command
`pip install flexy-probability-distributions-hApImAn`
or
`python3 -m pip install flexy-probability-distributions-hApImAn`
If everything is set up correctly, pip will install the distributions package into the workspace. You can then start the python interpreter from the terminal typing:
`python`
- then within the interpreter,  you can use the distributions package, for example:  
    ```python 
    from distributions import Gaussian, Binomial
    Gaussian(10, 7)
    Binomial(.5, 25)    
    ```

Thank you for checking this awesome distributions project out. Feel free to reach out if you have any question. 

Happy Coding! :)