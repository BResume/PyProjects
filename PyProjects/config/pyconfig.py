import os

class Config():

    def __init__(self,name):
        self._config_name = name

    @property
    def config_name(self):
        return self._config_name

    def make(self,temp_dir,data,filename):
        with open(temp_dir+filename,'w') as f:
            f.write(data)
            f.close()

class SetupInit(Config):
    
    def __init__(self,temp_dir,script = 'import os,sys\n\nsys.path.append(os.getcwd())'):
        self.make(temp_dir,script,'__init__.py')

class SetupPy(Config):
    
    def __init__(self,
        temp_dir,project_name,author,email,desc,url,project_urls,project_version='0.0.1',classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",],
        package_dir = {"": "src"},packages='setuptools.find_packages(where=\"src\")',requires=">=3.6",content_type='text/markdown'):
        super().__init__('setup.py')
        text = '''    
import setuptools

with open({0}/\"README.md\", \"r\", encoding=\"utf-8\") as fh:
    long_description = fh.read()

setuptools.setup(
    name={1}, # Replace with your own username
    version={2},
    author={3},
    author_email={4},
    description={5},
    long_description=long_description,
    long_description_content_type={12},
    url={6},
    project_urls={{
        {7}
    }},
    classifiers=[
        {8}
    ],
    package_dir={9},
    packages={10},
    python_requires={11},
)
        '''.format(temp_dir,project_name,project_version,author,email,desc,url,project_urls,classifiers,package_dir,packages,requires,content_type)
        self.make(temp_dir,text,'setup.py')

class SetupToml(Config):
    
    def __init__(self,temp_dir,requires = [
                "setuptools>=42",
                "wheel"], 
            build_backend = "setuptools.build_meta"):
    
        text = '''
[build-system]
requires = [
    {0}
]
build-backend = {1}
        '''.format(requires,build_backend)
        self.make(temp_dir,text,'pyproject.toml')

class SetupCFG(Config):
    
    def __init__(self,temp_dir,name,author,author_email,desc,readme,content_type='text/markdown',url='',version='0.0.1',project_urls = [''],
        classifiers = 'Programming Language :: Python :: 3 \nLicense :: OSI Approved :: MIT License \nOperating System :: OS Independent',
        package_dir = '= src', packages = 'find:',python_requires='>=3.6',where='src'):
        text = '''
[metadata]
# replace with your username:
name = {0}
version = {1}
author = {2}
author_email = {3}
description = {4}
long_description = {5}
long_description_content_type = {6}
url = {7}
project_urls =
    {8}
classifiers =
    {9}

[options]
package_dir = {10}
packages = {11}
python_requires = 
    {12}
[options.packages.find]
where = {13}
        '''
        self.make(temp_dir,text,'setup.cfg')

class SetupMain(Config):
    
    def __init__(self,temp_dir,project_name,script,other_classes):
        text = '''
from {0} import *

class Main():    
    def __init__(self):
        print("New PyProject!")
    
    def main():
        print("Hello World!") 
    
    {1}

{2}

if __name__ == '__main__':
    ma = Main
    ma.main()"
            '''.format(project_name,script,other_classes)
        self.make(temp_dir,text,'main.py')
        