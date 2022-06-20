from setuptools import setup, find_packages
import pathlib

setup(
    name='ti',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "ti=ti.clients.cli:cli"
        ]
    },
    install_requires=[
        "click",
        "requests",
        "pydantic",
    ],
    extras_require={
    },
    package_data={
        "": ["*.toml"],
    },
)
