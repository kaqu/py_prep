# py_prep

Simple python environment setup.

## Declare requirements

Write down package requirements inside requirements.py it will be installed via pip automatically.
You can declare additional packages for dev environments and minimal python interpreter version required.

## Run

To run use

``` bash
python -m py_prep -init
````

Available options:

`-init` - initializes environment and installs required packages

`-install` - installs required packages, requires valid environment

`-dev` - installs declared dev packages

`-no-venv` - do not require virtial environment - uses current environment for all operations

`-check` - checks if current enfironment meets requirements
