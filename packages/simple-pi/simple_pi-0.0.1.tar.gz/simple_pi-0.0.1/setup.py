from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simple_pi",
    version="0.0.1",
    author="Diego Soek",
    description="Simple pi package generator",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/dio-ciencia-de-dados/simple-pi",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)