from PyProjects.pyprojects import PyProjects

if __name__ == '__main__':
    proj = PyProjects()
    proj.make_project(os.getcwd()+'/Tests/','test_proj','test','test@test.com','test')