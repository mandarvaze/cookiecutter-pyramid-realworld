"""Installer for the {{cookiecutter.project_name}} package."""

from setuptools import find_packages
from setuptools import setup

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1",
    description="{{cookiecutter.project_name}}",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: MIT",
    ],
    author="Mandar Vaze",
    author_email="mndarvaze@gmail.com",
    url="http://github.com/mandarvaze/cookiecutter-pyramid-realworld",
    keywords="pyramid openapi realworld cookiecutter",
    license="MIT",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    entry_points="""\
    [paste.app_factory]
    main = {{cookiecutter.project_slug}}:main
    """,
    test_suite="{{cookiecutter.project_slug}}",
)
