from setuptools import setup

with open("Readme.md", "r") as readme_file:
    readme = readme_file.read()
    
with open("versions.txt", "r") as versions_file:
    ver = versions_file.read()

setup(
    name="converter",
    version=ver,
    
    author="Maria Maksimova",
    author_email="maryia.maksimava@yahoo.com",
    
    description="A package for converting temperature from Celsius to Fahrenheit and vise versa",
    license="MIT License",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/MariaMaximova/convert_temp",
    
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: Stable",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)
