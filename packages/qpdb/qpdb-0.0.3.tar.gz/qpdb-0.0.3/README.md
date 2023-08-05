# qu ⠶ pd

[![CI Status](https://github.com/qu-arx/qp/actions/workflows/master.yml/badge.svg)](https://github.com/qu-arx/qp/actions/workflows/master.yml)
[![Coverage](https://codecov.io/gh/qu-arx/qp/branch/master/graph/badge.svg)](https://codecov.io/github/qu-arx/qp)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Pandas API reference

## Motivation

To collect a database of the pandas API to enable gamified study,
or simple reference usage.

## Outline

- Either download docs as ZIP of HTML, or mine the package repo (parse RST with docutils to give
  doctrees). The latter would be preferable (but perhaps not useful since autosummary is used).
- Make sqlite3 database with fields: name (e.g. "DataFrame"), qualname prefix (e.g. "pandas"), type
  (e.g. "class"), and so on. This would amount to a 'walk' of the library's entity tree.
- Expose these entities in a structured way (as an entity tree).

## Possible applications

- 🐼 PQ Test: pandas API recall score, like an IQ test
- 🐼 PPM: typing test, for completing tasks in pandas

## Requires

- Python 3.10+

## Installation

```sh
pip install qpdb
```

> _qp_ is available from [PyPI](https://pypi.org/project/qpdb), and
> the code is on [GitHub](https://github.com/qu-arx/qp)
