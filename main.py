import os

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk

from PyProjects.pyprojects import PyProjects

class Main(PyProjects):

    def __init__(self):
        self._project_dir=os.getcwd()+'/Projects/Test/'
        self._project_name="Test"
        self._author='AUTHOR'
        self._email='example@email.com'
        self._desc='DESCRIPTION'
        self._url=''
        self._project_urls= []
        self._project_version= "0.0.1"
        self._classififers= "Programming Language :: Python :: 3\nLicense :: OSI Approved :: MIT License\nOperating System :: OS Independent"
        self._package_dir = {"": "src"}
        self._packages= "setuptools.find_packages(where=\"src\")"
        self._requires= ">=3.6"
        self._readme= "default_readme.txt"
        self._in_license= "default_license.txt"
        self._company_name= self.author
        self._paths= []
        self._static_requires=["setuptools>=42","wheel"], 
        self._build_backend="setuptools.build_meta"
        self._content_type="text/markdown"
        self._where="src"
        self._main_script="from {0} import *\n\nclass Main():\n\n    def __init__(self):\n        pass\n\nif __name__ == '__main__':\n    pass".format(self.where)
        self._init_script=""
        self._other_main_classes=""
        self._project_script = ""
        self._try_git = False

        self._window = tk.Tk()
        self._window.title("PyProjects")
        self._window.rowconfigure(1, minsize=800, weight=1)
        self._window.columnconfigure(1, minsize=800, weight=1)
        self._tabs = ttk.Notebook(self._window)
        self._fr_buttons = tk.Frame(self._tabs, relief=tk.RAISED, bd=2)
        self._btn_build = tk.Button(self._fr_buttons, text="Build", command=self.build)
        self._tabs.grid(row = 0, column = 0, stick = "ew",padx = 5, pady = 5)
        self._btn_build.grid(row=0, column=0, sticky="ew", padx=5, pady = 5)
        self._fr_buttons.grid(row=0, column=0, sticky="ns")
        self._try_git_cb = tk.Checkbutton(self._fr_buttons, text='Enable Git Push',variable=self.try_git, onvalue=1, offvalue=0, command=self.enable_git)
        self._try_git_cb.grid(row = 0,column = 1, stick = "ew",padx = 5, pady = 5)

        #Build tabs
        self._entry_window_p1 = self.scrollbox(self._tabs)
        self._entry_window_p2 = self.scrollbox(self._tabs)
        self._entry_window_p2g = self.scrollbox(self._tabs)
        self._entry_window_p3 = self.scrollbox(self._tabs)
        self._entry_window_p4 = self.scrollbox(self._tabs)
        self._entry_window_p5 = self.scrollbox(self._tabs)
        self._entry_window_p6 = self.scrollbox(self._tabs)
        self._entry_window_p7 = self.scrollbox(self._tabs)
        self._entry_window_p8 = self.scrollbox(self._tabs)
        self._entry_window_p9 = self.scrollbox(self._tabs)
        self._tabs.add(self._entry_window_p1,text = "Project")
        self._tabs.add(self._entry_window_p2,text = "Packaging")
        self._tabs.add(self._entry_window_p2g,text = "Git Settings")
        self._tabs.add(self._entry_window_p3,text = "Other")
        self._tabs.add(self._entry_window_p4,text = "README")
        self._tabs.add(self._entry_window_p5,text = "LICENSE")
        self._tabs.add(self._entry_window_p6,text = "Main Script")
        self._tabs.add(self._entry_window_p7,text = "Init Script")
        self._tabs.add(self._entry_window_p8,text = "Main Classes")
        self._tabs.add(self._entry_window_p9,text = "Project Script")
        self._tabs.add(self._fr_buttons,text = "Build")
        #self._tabs.pack(expand=1, fill="both")
        
        #Setup pages
        self._project_dir_entry = self.horizontal_box(self._entry_window_p1,self.open_set_project_dir,self.project_name,"Project Path")
        self._project_name_entry = self.horizontal_box(self._entry_window_p1,self.open_set_project_name,self.project_name,"Project Name",no_button = True)
        self._author_entry = self.horizontal_box(self._entry_window_p1,self.open_set_author,self.author,"Author",no_button = True)
        self._email_entry = self.horizontal_box(self._entry_window_p1,self.open_set_email,self.email,"Email",no_button = True)
        self._desc_entry = self.horizontal_box(self._entry_window_p1,self.open_set_desc,self.desc,"Description",False,no_button = True)
        self._url_entry = self.horizontal_box(self._entry_window_p2g,self.open_set_url,self.url,"URL",no_button = True)
        self._project_urls_entry = self.horizontal_box(self._entry_window_p2g,self.open_set_project_urls,self.project_urls,"Other URLS",False,no_button = True)
        self._project_version_entry = self.horizontal_box(self._entry_window_p1,self.open_set_project_version,self.project_version,"Project Version",no_button = True)
        self._classififers_entry = self.horizontal_box(self._entry_window_p3,self.open_set_classifiers,self.classififers,"Classifiers",False,no_button = True)
        self._package_dir_entry = self.horizontal_box(self._entry_window_p2,self.open_set_package_dir,self.package_dir,"Package Directory",no_button = True)
        self._packages_entry = self.horizontal_box(self._entry_window_p2,self.open_set_packages,self.packages,"Packages",False,no_button = True)
        self._requires_entry = self.horizontal_box(self._entry_window_p2,self.open_set_requires,self.requires,"Requires",no_button = True)
        self._readme_entry = self.horizontal_box(self._entry_window_p4,self.open_set_readme,self.readme,"README",False)
        self._in_license_entry = self.horizontal_box(self._entry_window_p5,self.open_set_in_license,self.in_license,"LICENSE",False)
        self._company_name_entry = self.horizontal_box(self._entry_window_p1,self.open_set_company_name,self.company_name,"Company Name",no_button = True)
        self._paths_entry = self.horizontal_box(self._entry_window_p3,self.open_set_paths,self.paths,"Other Program Directories",no_button = True)
        self._static_requires_entry = self.horizontal_box(self._entry_window_p3,self.open_set_static_requires,self.static_requires,"Static Requires",False,no_button = True)
        self._build_backend = self.horizontal_box(self._entry_window_p2,self.open_set_build_backend,self.build_backend,"Build Backend",no_button = True)
        self._content_type_entry = self.horizontal_box(self._entry_window_p4,self.open_set_content_type,self.content_type,"Long Description Content Type",no_button = True)
        self._where_entry = self.horizontal_box(self._entry_window_p2,self.open_set_where,self.where,"Main Directory",no_button = True)
        self._main_script_entry = self.horizontal_box(self._entry_window_p6,self.open_set_main_script,self.main_script,"Main Script",False)
        self._init_script_entry = self.horizontal_box(self._entry_window_p7,self.open_set_init_script,self.init_script,"Init Script",False)
        self._other_main_classes_entry = self.horizontal_box(self._entry_window_p8,self.open_set_other_main_classes,self.other_main_classes,"Other Main Classes",False)
        self._project_script_entry = self.horizontal_box(self._entry_window_p9,self.open_set_project_script,self.project_script,"Project Script",False)  

        self._project_name_entry.pack() 
        self._author_entry.pack()
        self._email_entry.pack()
        self._desc_entry.pack()
        self._url_entry.pack()
        self._project_urls_entry.pack()
        self._project_version_entry.pack()
        self._classififers_entry.pack()
        self._package_dir_entry.pack()
        self._packages_entry.pack()
        self._requires_entry.pack()
        self._readme_entry.pack()
        self._in_license_entry.pack()
        self._company_name_entry.pack()
        self._paths_entry.pack()
        self._static_requires_entry.pack()
        self._build_backend.pack()
        self._content_type_entry.pack()
        self._where_entry.pack()
        self._main_script_entry.pack()
        self._init_script_entry.pack()
        self._other_main_classes_entry.pack()
        self._project_script_entry.pack()   
    
    @property
    def project_dir(self):        
        return self._project_dir
    
    @property
    def project_name(self):        
        return self._project_name
    
    @property
    def author(self):        
        return self._author

    @property
    def email(self):        
        return self._email
    
    @property
    def desc(self):        
        return self._desc

    @property
    def url(self):        
        return self._url

    @property
    def project_urls(self):        
        return self._project_urls

    @property
    def project_version(self):        
        return self._project_version

    @property
    def classififers(self):        
        return self._classififers
    
    @property
    def package_dir(self):        
        return self._package_dir

    @property
    def packages(self):        
        return self._packages

    @property
    def requires(self):        
        return self._requires

    @property
    def readme(self):        
        return self._readme

    @property
    def in_license(self):        
        return self._in_license

    @property
    def company_name(self):      
        if self._company_name == '':
            return self._author
        else:  
            return self._company_name

    @property
    def paths(self):        
        return self._paths

    @property
    def static_requires(self):        
        return self._static_requires

    @property
    def build_backend(self):        
        return self._build_backend

    @property
    def content_type(self):        
        return self._content_type

    @property
    def where(self):        
        return self._where
    
    @property
    def main_script(self):        
        return self._main_script
    
    @property   
    def init_script(self):        
        return self._init_script
    
    @property
    def other_main_classes(self):        
        return self._other_main_classes
    
    @property
    def project_script(self):
        return self._project_script

    @property
    def try_git(self):
        return self._try_git

    def scrollbox(self,parent,side=RIGHT,fill=Y)):
        frame = ttk.Frame(parent)
        # implementing scrollbar functionality
        scrollbar = Scrollbar(frame)
        # packing the scrollbar function
        scrollbar.pack(side = side, fill = fill)
        return frame

    def enable_git(self):
        self._try_git = self._try_git_cb.get()

    def horizontal_box(self,window,command,value,title,single_line = True,
        fg = "black",bg = "white",bbg = "blue", bfg = "yellow", width = 50, sticky = 'ew',padx = 5, pady = 5,
        no_button = False,foreground="blue",background="black"):
        frame = tk.Frame(window)
        ttl = tk.Label(frame,text=title,foreground="white",background="black")
        frame.rowconfigure(1, minsize=10, weight=1)
        frame.columnconfigure(1, minsize=10, weight=1)
        if single_line:
            entry = tk.Entry(frame,fg=fg, bg=bg, width=width) 
        else:
            entry = tk.Text(frame)
        entry.insert(tk.END,value)
        entry.grid(row=1, column=0, sticky=sticky, padx=padx, pady=pady)
        ttl.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)
        if not no_button:
            button = tk.Button(frame,text=title,width=25,height=1,bg=bbg,fg=bfg,command = command)
            button.grid(row=1, column=1, sticky=sticky, padx=padx, pady=pady)
        frame.pack(fill='both')
        return frame

    def main(self):
        self._window.mainloop()

    def open_set_project_dir(self):
        self._project_dir = self.set_entry(self._project_dir_entry)

    def open_set_project_name(self):
        self._project_name = self.set_entry(self._project_name_entry)

    def open_set_author(self):
        self._author = self.set_entry(self._author_entry)

    def open_set_email(self):
        self._email = self.set_entry(self._email_entry)

    def open_set_desc(self):
        self._desc = self.set_entry(self._desc_entry)

    def open_set_url(self):
        self._url = self.set_entry(self._url_entry)

    def open_set_project_urls(self):
        self._project_urls = self.set_entry(self._project_urls_entry)

    def open_set_project_version(self):
        self._project_version = self.set_entry(self._project_version_entry)

    def open_set_classifiers(self):
        self._classififers = self.set_entry(self._classifiers_entry)

    def open_set_package_dir(self):
        self._package_dir = self.set_entry(self._package_dir_entry)

    def open_set_packages(self):
        self._packages = self.set_entry(self._packages_entry)

    def open_set_requires(self):
        self._requires = self.set_entry(self._requires_entry)

    def open_set_readme(self):
        self._readme = self.set_entry(self._readme_entry,True)

    def open_set_in_license(self):
        self._in_license = self.set_entry(self._in_license_entry,True)

    def open_set_company_name(self):
        self._company_name = self.set_entry(self._company_name_entry)

    def open_set_paths(self):
        self._paths = self.set_entry(self._paths_entry,True)

    def open_set_static_requires(self):
        self._static_requires = self.set_entry(self._static_requires_entry,True)

    def open_set_build_backend(self):
        self._build_backend = self.set_entry(self._build_backend_entry)

    def open_set_content_type(self):
        self._content_type = self.set_entry(self._content_type_entry)

    def open_set_where(self):
        self._where = self.set_entry(self._where_entry)
        self._package_dir = "{"":{0}}".format(self.where)
        self.set_entry(self._package_dir_entry)

    def open_set_main_script(self):
        self._main_script = self.set_entry(self._main_script_entry,True,[("Python", "*.py")])

    def open_set_init_script(self):
        self._init_script = self.set_entry(self._init_script_entry,True,[("Python", "*.py")])

    def open_set_other_main_classes(self):
        self._other_main_classes = self.other_main_classes_entry(self._other_main_classes_entry,True,[("Python", "*.py")])

    def open_set_project_script(self):
        self._project_script = self.set_entry(self._project_script_entry,True,[("Python", "*.py")])

    def set_entry(self,entry,no_txt = True,filetypes =[("Text Files", "*.txt"), ("All Files", "*.*")]):
        txt = None
        if not no_txt:
            txt = entry
        var = self.open_file(no_txt,txt,filetypes)
        #entry.delete(1.0,tk.END)
        #entry.insert(tk.END,self._project_script)
        return var

    def open_file(self,return_path = True,txt = None,filetypes =[("Text Files", "*.txt"), ("All Files", "*.*")]):
        """Open a file or select a directory."""
        filepath = askopenfilename(filetypes=filetypes)
        if not filepath:
            return
        if not txt == None:
            txt.delete(1.0, tk.END)
            with open(filepath, "r") as input_file:
                text = input_file.read()
                txt.insert(tk.END, text)
        output = text
        if return_path:
            output = filedialog.askdirectory()
        return output

    def build(self):
        '''
        self._project_name = self._project_name_entry.get() 
        self._email = self._author_entry.get()
        self._email = self._email_entry.get()
        self._desc = self._desc_entry.get()
        self._url = self._url_entry.get()
        self._project_urls = self._project_urls_entry.get()
        self._project_version = self._project_version_entry.get()
        self._classififers = self._classififers_entry.get()
        self._package_dir = self._package_dir_entry.get()
        self._packages = self._packages_entry.get()
        self._requires = self._requires_entry.get()
        self._readme = self._readme_entry.get()
        self._in_license = self._in_license_entry.get()
        self._company_name = self._company_name_entry.get()
        self._paths = self._paths_entry.get()
        self._static_requires = self._static_requires_entry.get()
        self._build_backend = self._build_backend.get()
        self._content_type = self._content_type_entry.get()
        self._where = self._where_entry.get()
        self._main_script = self._main_script_entry.get()
        self._init_script = self._init_script_entry.get()
        self._other_main_classes = self._other_main_classes_entry.get()
        self._project_script = self._project_script_entry.get()    
        '''
        self.make_project(self.project_dir,self.project_name,self.author,self.email,self.desc,self.url,self.project_urls,
            self.project_version,self.classififers,self.package_dir,self.packages,self.requires,self.readme,
            self.in_license,self.company_name,self.paths,
            self.static_requires,self.build_backend,
            self.content_type,self.where,self.main_script,self.init_script,self.other_main_classes,self.project_script,self.try_git)

if __name__ == '__main__':
    ma = Main()
    ma.main()
    