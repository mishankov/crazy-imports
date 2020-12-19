# Crazy Imports - treat your data as your code


![CI](https://github.com/mishankov/crazy-imports/workflows/CI/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/mishankov/crazy-imports/actions?query=workflow%3Ablack)
[![PyPI](https://img.shields.io/pypi/v/crazyimports)](https://pypi.org/project/crazyimports/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/crazyimports)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/crazyimports)
[![PyPI - License](https://img.shields.io/pypi/l/crazyimports)](https://github.com/mishankov/crazy-imports/blob/main/LICENSE)

`crazyimports` module allows you to use your data files as if it was python modules

## Installation

`pip install crazyimports`

## Simple example

Create `example.json` file with this content

```json
{"number": 42}
```

 Than in the same directory create `test.py` file

```python
import crazyimports.json
import example

print(example.number)
```

Then when you run `python test.py` you would see `42` output in your command line

This and other examples you can find in `examples/` folder

## Supported file extensions

- `.json` for JSON files
- `.sqlite3` for SQLite3 database files
- `.csv` for CSV (Comma Separated Values) files
- `.yaml` for YAML files

## Inspiration

Heavily inspired by [this talk](https://youtu.be/CWZVNgStgbI) by [@bobuk](https://github.com/bobuk)
