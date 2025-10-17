# before install requirements.txt fill this setup file


import setuptools

# Read the contents of your README file -help when publishing PyPI package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0" # Define version here

REPO_NAME = "deeplearning" #repository name
AUTHOR_USER_NAME = "tez7" #github username
SRC_REPO = "classification_task" #source repo name

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for deeplearnig app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)