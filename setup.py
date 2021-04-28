from setuptools import setup, find_packages

packages = find_packages(exclude=['tests*'])

setup(
    name='formio-data',
    version='0.2.4',
    description='Form.io JSON-data API',
    url='https://github.com/novacode-nl/python-formio-data',
    author='Bob Leers',
    author_email='bob@novacode.nl',
    license='MIT',
    packages=packages
 )
