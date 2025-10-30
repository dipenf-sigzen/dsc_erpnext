from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")


setup(
    name='dsc_erpnext',
    version='0.0.1',
    description='Custom ERPNext app',
    author='Your Name',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)
