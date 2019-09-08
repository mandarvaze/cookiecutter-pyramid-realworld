# Getting started

You need to have docker, [pipenv](https://pipenv.readthedocs.io/) and Python 3.7 installed on your machine. Docker should be running. Then you can run:

``` shell
$ cd {{cookiecutter.project_slug}}
$ git init
$ make install
$ pipenv install -e .
$ make start-pgsql
$ make devdb
$ make run
```

Now point your browser to:
 * http://localhost:8080/api -> Swagger documentation for the API


To run unit tests, mypy typing checker and flake8 linter:

`$ make tests`

To stop docker and clean container, you can run:

``` shell
$ make stop-pgsql
$ make clean-pgsql
```