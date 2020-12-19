# Crazy Imports - treat your data as your code

[![CI/CD](https://github.com/mishankov/crazy-imports/workflows/CI/CD/badge.svg)](https://github.com/mishankov/crazy-imports/actions?query=workflow:CI/CD)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/mishankov/crazy-imports/actions?query=workflow:CI/CD)
[![PyPI](https://img.shields.io/pypi/v/crazyimports)](https://pypi.org/project/crazyimports/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/crazyimports)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/crazyimports)
[![PyPI - License](https://img.shields.io/pypi/l/crazyimports)](https://github.com/mishankov/crazy-imports/blob/main/LICENSE)

`crazyimports` module allows you to use your data files as if it was python modules

- [Documentation](https://mishankov.github.io/crazy-imports/)
- [GitHub repo](https://github.com/mishankov/crazy-imports)

## Simple example

Install `crazyimports` module

`pip install -U crazyimports`

Create `example.json` file with this content

```json
{"number": 42}
```

 Than in the same directory create `test.py` file

```python
import crazyimports
import example

print(example.number)
```

Then when you run `python test.py` you would see `42` output in your command line

You can find more examles in exaples section of [documentation](https://mishankov.github.io/crazy-imports/)

## Supported file extensions

- `.json` for JSON files
- `.sqlite3` and `.sqlite` for SQLite3 database files
- `.csv` for CSV (Comma Separated Values) files
- `.yaml` and `.yml` for YAML files

## Credits

Heavily inspired by [this talk](https://youtu.be/CWZVNgStgbI) by [@bobuk](https://github.com/bobuk)
