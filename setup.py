from setuptools import setup, find_packages

setup(
    name="file-compression-tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt5>=5.15.11",
        "pytest>=7.3.1",
        "coverage>=7.2.7",
    ],
) 