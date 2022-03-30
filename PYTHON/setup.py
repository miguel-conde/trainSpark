# https://medium.com/analytics-vidhya/data-directory-in-jupyter-notebooks-dc46cd79eb2f
#
# python -m pip install -e .
#
# Tb: 
#       - https://pythonhosted.org/an_example_pypi_project/setuptools.html
#       - https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/

from setuptools import setup, find_packages

setup(
    name="prjmod",
    packages=find_packages(),
)