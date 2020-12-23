# Contributing to Crazy Imports

## Project structure

- `/crazyimports` - module itself
- `/examples` - examples of using crazyimports
- `/tests` - tests for crazyimports
- `/docs` - markdown files to generate documentation with `mkdocs`

## Useful commands

First, you need to install all dev depenencies

```bash
make install-dev
```

After you made changes and wrote tests for them, run the tests

```bash
make test
```

Before commit run this to make sure your code is properly formatted and documentation is up to date

```bash
make prepare-push
```
