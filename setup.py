from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.1"
REPO_NAME = "mongodbconnectorpkg"
PKG_NAME= "databaseautomation"
AUTHOR_USER_NAME = "Gaurab"
AUTHOR_EMAIL = "gaurabchoudhary2002@gmail.com"

def get_requirements(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
    
setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = get_requirements("./requirements_dev.txt")

    )