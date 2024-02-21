from setuptools import setup, find_packages

setup(
    name='taskmaster',
    version='0.1',
    description='A simple command-line task management application',
    author='Ravenium22',
    author_email='efeberkakgul@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'taskmaster = taskmaster.taskmaster:main',
        ],
    },
    install_requires=[
        # List your dependencies here
    ],
)
