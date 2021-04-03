import os,sys
try:
    from PyProjects.config.pyconfig import *
except ImportError as e:
    from config.pyconfig import *


class PyProjects():

    def __init__(self):
        pass

    '''
        Create the setup.py file.
        @PARAM: temp_dir = The dir that the file is created in.
        @PARAM: project_name = The Project name.
        @PARAM: author = The project's author.
        @PARAM: author_email = The email for the project's author.
        @PARAM: desc = Project description.
        @PARAM: url = The project's url.
        @PARAM: project_urls = The project's urls.
        @PARAM: project_version = The project version.
        @PARAM: readme = The README.md as text, not as a file.
        @PARAM: classifiers = Project classifiers.
        @PARAM: package_dir = The location of the package.
        @PARAM: packages = The project packages.
        @PARAM: requires = The project dependencies.
        @PARAM: content_type = The long_description content type.
    '''
    def setup_py(self,
        temp_dir,project_name,author,email,desc,url='',project_urls=[''],project_version='0.0.1',classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",],
        package_dir = {"": "src"},packages='setuptools.find_packages(where=\"src\")',requires=">=3.6",content_type='text/markdown'):
        setup = SetupPy(temp_dir,project_name,author,email,desc,url,project_urls,project_version,classifiers,package_dir,packages,requires,content_type)       

    '''
        Create the setup.cfg file.
        @PARAM: temp_dir = The dir that the file is created in.
        @PARAM: name = The Project name.
        @PARAM: author = The project's author.
        @PARAM: author_email = The email for the project's author.
        @PARAM: desc = Project description.
        @PARAM: readme = The README.md as text, not as a file.
        @PARAM: content_type = The long_description content type.
        @PARAM: url = The project's url.
        @PARAM: version = The project version.
        @PARAM: project_urls = The project's urls.
        @PARAM: classifiers = Project classifiers.
        @PARAM: package_dir = The location of the package.
        @PARAM: packages = The project packages.
        @PARAM: python_requires = The project dependencies.
        @PARAM: where = The location of the project files.
    '''
    def setup_cfg(self,temp_dir,name,author,author_email,desc,readme,content_type='text/markdown',url='',version='0.0.1',project_urls = [''],
        classifiers = 'Programming Language :: Python :: 3 \nLicense :: OSI Approved :: MIT License \nOperating System :: OS Independent',
        package_dir = '= src', packages = 'find:',python_requires='>=3.6',where='src'):
        setup = SetupCFG(temp_dir,name,author,author_email,desc,readme,content_type,url,version,project_urls,classifiers,package_dir,packages,python_requires,where)

    '''
        Create the pyprojects.toml file.
        @PARAM: temp_dir = The dir that the file is created in.
        @PARAM: requires = The requirements for the program.
        @PARAM: build_backend = The build backend.
    '''
    def setup_toml(self,temp_dir,requires,build_backend):
        setup = SetupToml(temp_dir,requires,build_backend)

    '''
        Create the main script.
        @PARAM: temp_dir = The dir that the file is created in.
        @PARAM: project_name = The name of the project.
        @PARAM: script = More functions to add to the Main() class.
        @PARAM: other_classes = More classes to add to main.py. They must contain an init function or the program won't compile.
    '''
    def setup_main(self,temp_dir,project_name,script,other_classes):
        setup = SetupMain(temp_dir,project_name,script,other_classes)

    '''
        Helper to create the __init__.py file.
        @PARAM: temp_dir = The dir that the file is created in.
        @PARAM: script = The script to go in the file.
    '''
    def setup_init(self,temp_dir,script):
        setup = SetupInit(temp_dir,script)

    def read_or_load(self,data,condition,in_file,company_name,default, replacements = {
        "[COMPANYNAME]":'company_name'}
        ):
        output = ''
        if data == condition:
            with open (in_file,'r') as f:
                output = f.read()
                for replacer,replacee in replacements.items():
                    if replacee == 'company_name':
                        replacee = company_name
                    if replacer in output:
                        output = output.replace(replacer,replacee)
        elif os.path.isfile(data):
            with open (data,'r') as f:
                output = f.read()
        else:
            return default
        return output

    '''
        Create the setup.py file.
        @PARAM: temp_dir = The dir that the file is created in.
        @PARAM: project_name = The Project name.
        @PARAM: author = The project's author.
        @PARAM: author_email = The email for the project's author.
        @PARAM: desc = Project description.
        @PARAM: url = The project's url.
        @PARAM: project_urls = The project's urls.
        @PARAM: project_version = The project version.
        @PARAM: classifiers = Project classifiers.
        @PARAM: package_dir = The location of the package.
        @PARAM: packages = The project package locations.
        @PARAM: requires = The required python version.
        @PARAM: readme = The readme to add to the project file. If left default it will read the default_license.txt file in the config directory. It can be a file or full text.
        @PARAM: in_license = The license to add to the project file. If left default it will read the default_license.txt file in the config directory. It can be a file or full text.
        @PARAM: company_name = The company's name.
        @PARAM: paths = Additional directories to add to the project when created. If [] is in the directory name it will be added as a child of the where directory.
        @PARAM: static_requires = The requirements for the program.
        @PARAM: build_backend = The build backend.
        @PARAM: content_type = The long_description content type.
        @PARAM: where = The location of the project files.
        @PARAM: main_script = Functions to add to the Main() class.
        @PARAM: init_script = The script to go in the file.
        @PARAM: other_classes = More classes to add to main.py. They must contain an init function or the program won't compile.
        @PARAM: project_script = The custom project script.
    '''
    def make_project(self,
        temp_dir,project_name,author,email,desc,url='',project_urls=[''],
        project_version='0.0.1',classifiers=[
            "Programming Language :: Python :: 3\nLicense :: OSI Approved :: MIT License\nOperating System :: OS Independent"
        ],
        package_dir = {
            "": "src"
        },
        packages='setuptools.find_packages(where=\"src\")',requires=">=3.6",
        readme = 'default_readme.txt',in_license = 'default_license.txt',company_name='',paths = [],
        static_requires = [
                "setuptools>=42",
                "wheel"
            ], 
        build_backend = "setuptools.build_meta",content_type = 'text/markdown',where='src',main_script = '',init_script = '',other_main_classes = '',
        project_script = '',try_git = False):
        if company_name == '':
            company_name = author
        '''
        if readme == 'default_readme.txt':
            with open(os.getcwd()+'/PyProjects/config/default_readme.txt','r') as f:
                readme = f.read()
        elif os.path.isfile(readme):
            with open(readme,'r') as f:
                readme = f.read()
        if in_license == 'default_license.txt':
            with open (os.getcwd()+'/PyProjects/config/default_license.txt','r') as f:
                in_license = f.read()
                in_license.replace('[COMPANYNAME]',company_name)
        elif os.path.isfile(in_license):
            with open (in_license,'r') as f:
                in_license = f.read()
        '''
        readme = self.read_or_load(readme,'default_readme.txt',os.getcwd()+'/PyProjects/config/default_readme.txt',company_name,readme)
        in_license = self.read_or_load(in_license,'default_license.txt',os.getcwd()+'/PyProjects/config/default_license.txt',company_name,in_license)
        main_script = self.read_or_load(main_script,'default_main.txt',os.getcwd()+'/PyProjects/config/default_main.txt',company_name,main_script)
        init_script = self.read_or_load(in_license,'default_init.txt',os.getcwd()+'/PyProjects/config/default_init.txt',company_name,init_script)
        project_script = self.read_or_load(readme,'default_project.txt',os.getcwd()+'/PyProjects/config/default_project.txt',company_name,project_script)
        other_main_classes = self.read_or_load(in_license,'default_other_main.txt',os.getcwd()+'/PyProjects/config/default_other_main.txt',
            company_name,other_main_classes)
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)
        if not os.path.exists(temp_dir+where):
            os.mkdir(temp_dir+where)
        self.setup_init(temp_dir+where+'/',init_script)
        for path in paths:
            if '[]' in path:
                dire = where+path.replace('[]','/')
            else:
                dire = temp_dir+path
            os.mkdir(dire)
            setup_init(dire,init_script)
        with open(temp_dir+'/README.md','w') as f:
            f.write(readme)
        with open(temp_dir+'/LICENSE.md','w') as f:
            f.write(in_license)
        with open(os.getcwd()+'/PyProjects/config/.gitignore','r') as f:
            data = f.read()            
        with open(temp_dir+'/.gitignore','w') as f:
            f.write(data)
        with open(temp_dir+'/'+where+'/'+project_name+'.py','w') as f:
            f.write(project_script)
        self.setup_py(temp_dir,project_name,author,email,desc,url,project_urls,project_version,classifiers,package_dir,packages,requires,content_type)
        self.setup_cfg(temp_dir,project_name,author,email,desc,readme,content_type,url,project_version,project_urls,classifiers,package_dir,packages,static_requires,where)
        self.setup_toml(temp_dir,requires,build_backend)
        self.setup_main(temp_dir,project_name,main_script,other_main_classes)
        if try_git:
            GIT_COMMANDS = [
                "cd [temp_dir] && git init",
                "cd [temp_dir] && git commit -m \"first commit\"",
                "cd [temp_dir] && git branch -M main",
                "cd [temp_dir] && git remote add origin [url]",
                "cd [temp_dir] && git push -u origin main"
            ]
            for command in GIT_COMMANDS:
                do = command
                do.replace('[temp_dir]',temp_dir)
                if '[url]' in do:
                    do.replace('[url]',url)
                os.system(do)

def check_args(args,index,default = ''):
    if len(args)>=index:
        return args[index]
    else:
        return default

if __name__ == '__main__':
    proj = PyProjects()
    args = sys.argv 
    if len(args) > 1:
        if os.path.exists(args[0]):
            import json
            with open (args[0],'r') as f:
                index = 0
                if len(args) > 2:
                    index = args[1]
                data = json.load(f)
                temp_dir = data[index]['DIRECTIORY']
                project_name = data[index]['PROJECT_NAME']
                author = data[index]['AUTHOR']
                email = data[index]['EMAIL']
                desc = data[index]['DESCRIPTION']
                url = data[index]['URL']
                project_urls = data[index]['PROJECT_URLS']
                project_version = data[index]['PROJECT_VERSION']
                classifiers = data[index]['CLASSIFIERS']
                package_dir = data[index]['PACKAGE_DIRECTORIES']
                packages = data[index]['PACKAGES']
                requires = data[index]['REQUIRES']
                readme = data[index]['README']
                in_license = data[index]['LICENSE']
                company_name = data[index]['COMPANY_NAME']
                paths = data[index]['PATHS']
                static_requires = data[index]['STATIC_REQUIRES']
                build_backend = data[index]['BUILD_BACKEND']
                content_type = data[index]['CONTENT_TYPE']
                where = data[index]['WHERE']
                main_script = data[index]['MAIN_SCRIPT']
                init_script = data[index]['INIT_SCRIPT']
                other_main_classes = data[index]['OTHER_MAIN_CLASSES']
                project_script = data[index]['PROJECT_SCRIPT'] 
        else: 
            temp_dir = check_args(args,0)
            project_name = check_args(args,1)
            author = check_args(args,2)
            email = check_args(args,3)
            desc = check_args(args,4)
            url = check_args(args,5)
            project_urls = check_args(args,6)
            project_version = check_args(args,7)
            classifiers = check_args(args,8)
            package_dir = check_args(args,9)
            packages = check_args(args,10)
            requires = check_args(args,11)
            readme = check_args(args,12)
            in_license = check_args(args,13)
            company_name = check_args(args,14)
            paths = check_args(args,15)
            static_requires = check_args(args,16) 
            build_backend = check_args(args,17)
            content_type = check_args(args,18)
            where = check_args(args,19)
            main_script = check_args(args,20)
            init_script = check_args(args,21)
            other_main_classes = check_args(args,22)
            project_script = check_args(args,23)
        proj.make_project(temp_dir,project_name,author,email,desc,url,project_urls,project_version,classififers,package_dir,packages,requires,readme,
            in_license,company_name,paths,static_requires,build_backend,content_type,where,main_script,init_script,other_main_classes,project_script)
    else:
        proj.make_project(os.getcwd()+'/Tests/test_proj/','test_proj','test','test@test.com','test')
