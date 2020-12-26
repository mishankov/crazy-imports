# Contributing to Crazy Imports

## Project structure

- `/crazyimports` - module itself
- `/examples` - examplese of using crazyimports
- `/tests` - tests for crazyimports
- `/docs` - markdown files to generate documentation with `mkdocs`

## Useful commands

First, you need to prepare development environment

```bash
make dev-env
```

After you made changes and wrote tests for them, run the tests

```bash
make dev-test
```

Before commit run this to make sure your code is properly formatted and documentation is up to date

```bash
make dev-prepare-push
```
