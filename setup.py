from setuptools import setup, find_packages

setup(
    name="haplonggener",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyfaidx",
        "edlib",
    ],
    entry_points={
        "console_scripts": [
            "haplonggener=haplonggener.cli:main"
        ]
    },
)
