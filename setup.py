from setuptools import setup, find_packages

with open("Readme.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="converter",
    version="1.0.1",
    
    author="Maria Maksimova",
    author_email="maryia.maksimava@yahoo.com",
    
    description="A package to converting temperature from Celsius to Fahrenheit and vise versa",
    license="MIT License",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/MariaMaximova/convert_temp",
    classifiers=[
        "Development Status :: Stable",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)
