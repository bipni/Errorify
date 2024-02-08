from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    description = f.read()

setup(
    name='errorify',
    version='0.0.0',
    description='A Python package for structured error handling and formatting.',
    author='Bipu Mirza',
    author_email='bipumirja@gmail.com',
    packages=find_packages(),
    python_requires='>=3.0',
    long_description=description,
    long_description_content_type='text/markdown'
)
