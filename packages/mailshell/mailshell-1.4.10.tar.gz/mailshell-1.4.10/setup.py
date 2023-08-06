import pip
from re import sub
from pathlib import Path
from setuptools import setup
from setuptools import find_packages


# read long description from README file 
current_folder = Path(__file__).parent
README = sub('<img.+>', '', (current_folder / "README.md").read_text())

# get the requirements
REQUIREMENTS = (current_folder / "requirements.txt").read_text().splitlines()

setup(
    name="mailshell",
    version="1.4.10",
    author="Malki Abderrahman",
    author_email="abdo.malkiep@gmail.com",
    description="Send and check emails faster from the terminal",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/malkiAbdoo/mailshell",
    project_urls={
        'Source': 'https://github.com/malkiAbdoo/mailshell',
        'Tracker': 'https://github.com/joelibaceta/mailshell/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License"
    ],
    keywords="terminal, app, email, gmail, shell",
    entry_points={
        "console_scripts": ['msl=mailshell.app:main']
    }
)
