# glowgreen
A small Python package for calculating radiation dose from close contact patterns with radioactive patients. 

## Requires
- Python >= 3.9

## Installation
Install the package from the Python Package Index (PyPI) using pip:

    python -m pip install --upgrade glowgreen

Alternatively, if you have a clone of the repository on your local computer, you can install it via the *pyproject.toml* file.
First update your pip:

    python -m pip install --upgrade pip

Then enter e.g.:

    python -m pip install -e \path\to\glowgreen-master\

These are the preferred methods as they handle the dependencies for you. 
Another way is to add the **glowgreen-master\src** directory to the PYTHONPATH environment variable. For example, for Windows:

    set PYTHONPATH=%PYTHONPATH%;\path\to\glowgreen-master\src\

## Dependencies
- Python packages
    - numpy
    - scipy
    - matplotlib
    - pandas

## Testing
You can run some tests if there is a clone of the repository on your local computer. Install pytest:

    python -m pip install --upgrade pytest

Then in the **glowgreen-master** directory run:

    python -m pytest

## Documentation
Documentation including API reference can be generated using sphinx. 
If the **docs/source/** directory does not exist, see *HOWTO_documentation.md* to generate the documentation from scratch.
Otherwise, do the following:

Check the project information is up-to-date in *docs/source/conf.py*.

Install sphinx:

    python -m pip install sphinx

Github does not have empty directories **docs/source/_static** and **docs/source/_templates**.
Optionally create these empty directories to avoid a warning in the next step.

In **docs** directory, run:

    make html

The documentation is hosted on ReadTheDocs.
See https://sphinx-rtd-tutorial.readthedocs.io/en/latest/read-the-docs.html.

## Source 
https://github.com/SAMI-Medical-Physics/glowgreen

## Bug tracker
https://github.com/SAMI-Medical-Physics/glowgreen/issues

## Author
Jake Forster (jake.forster@sa.gov.au)

## Copyright
glowgreen is Copyright (C) 2022 South Australia Medical Imaging.

## License
MIT. See LICENSE file.

## Publications
Papers that use glowgreen:
* Close contact restriction periods for patients who received radioactive iodine-131 therapy for differentiated thyroid cancer, J. C. Forster et al., In preparation.
