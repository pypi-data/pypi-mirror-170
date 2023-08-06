import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="django-onepage",
    version="1.2.2",
    description="Django Onepage Application Management",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/njnafir/django-onepage",
    author="Nj Nafir",
    author_email="njnafir@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=['onepage', 'onepage.templates', 'onepage.static'],
    include_package_data=True,
    package_data={'templates': ['*'], 'static': ['*']},
    install_requires=['django', 'django-widget-tweaks'],
)
