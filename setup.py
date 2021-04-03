import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyProjects", # Replace with your own username
    version="0.0.1",
    author="behronsresume",
    author_email="behronsresume@gmail.com",
    description="Create a project.",
    long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/BResume/pyprojects",
    project_urls={
        "Bug Tracker": "https://github.com/BResume/pyprojects/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "PyProjects"},
    packages=setuptools.find_packages(where="PyProjects"),
    python_requires=">=3.6",
)
