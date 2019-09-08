# Cookiecutter Template for realworld app

This template is based on [Pyramid Realworld Example App](https://github.com/niteoweb/pyramid-realworld-example-app)

The Pyramid Realworld Example App has gone to great lengths to adhere to the **Pyramid** community styleguides & best practices. But using it as github scaffold/template for your next Pyramid project meant after you've created your project, you need to go and **remove** lot of unwanted code (Not every app has articles and comments). It also means you need to replace (at least) `conduit` (and `Conduit`) with your own project name. cookiecutter approach helps with the second issue.

**Please star the original [Pyramid Realworld Example App](https://github.com/niteoweb/pyramid-realworld-example-app) repo.**

# Getting started

You need to have [cookiecutter](https://pypi.python.org/pypi/cookiecutter), docker, [pipenv](https://pipenv.readthedocs.io/) and Python 3.7 installed on your machine. Docker should be running. Then you can run:

``` shell
$ cookiecutter https://github.com/mandarvaze/cookiecutter-pyramid-realworld
$ cd <project_slug>
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

# Thanks

* Pyramid community for making such an amazing [framework](https://docs.pylonsproject.org/projects/pyramid/en/latest/index.html)
* [Team Niteo](https://github.com/niteoweb/pyramid-realworld-example-app/graphs/contributors) for making the Pyramid Realworld Example App
* pydanny, audreyr and [others](https://github.com/cookiecutter/cookiecutter/graphs/contributors) for making cookiecutter.
