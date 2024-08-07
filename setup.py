 # IntegrationAPI/setup.py

from setuptools import setup, find_packages
from pathlib import Path


this_directory = Path(__file__).parent
setup(
    name="UnifyAPI",
    version="0.1.0",
    long_description=(this_directory / "README.md").read_text(),
    description="Python package for integrating with various APIs.",
    author="Sirisha Jotheeswaran Padmasekhar",
    author_email="sirishajpadmasekhar@gmail.com",
    packages=find_packages(),
    install_requires=[
        "tweepy",
        "paypalrestsdk",
        "googlemaps",
    ],
)