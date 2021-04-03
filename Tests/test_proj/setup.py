    
import setuptools

with open(/home/sen/ProjectFiles/Python/PyProjects/Tests/test_proj//"README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=test_proj, # Replace with your own username
    version=0.0.1,
    author=test,
    author_email=test@test.com,
    description=test,
    long_description=long_description,
    long_description_content_type=text/markdown,
    url=,
    project_urls={
        ['']
    },
    classifiers=[
        ['Programming Language :: Python :: 3\nLicense :: OSI Approved :: MIT License\nOperating System :: OS Independent']
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where="src"),
    python_requires=>=3.6,
)
        