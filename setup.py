from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
 
REPO_NAME = "NLP-STACKOVERFLOW-CLASSIFICATION"
AUTHOR_USER_NAME = "pranavrelds"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['tqdm', 'dvc[s3]', 'pandas', 'numpy', 'PyYAML', 'scikit-learn', 'Scipy', 'rich']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A classification solutions for stackoverflow questions for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="sunny.c17hawke@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)