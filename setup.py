from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''Returns a list of requirements'''
    requirements_list:List[str] = []
    # with open("requirements.txt") as f:
    #     requirements_list=f.read().splitlines()
    return requirements_list

setup(

    name="sensor",
    version="0.01",
    author="siddhant",
    author_email="siddhantbhagat46@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements(),
)