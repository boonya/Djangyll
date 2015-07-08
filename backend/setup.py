"""
Djangyll setup script.
"""

from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name='Djangyll',
    version='0.0.1',
    url='https://github.com/boonya/Djangyll',
    license='MIT',
    author='Sergii boonya Buinytskyi',
    author_email='boonya41@gmail.com',
    description='Yet another Content Management System',
    long_description='CMS for Jekyll bases static web sites.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'djangyll = scripts.manage:main',
        ]
    }
)
