# YAML

Create file with the name `config.toml`

```toml
number = 42
```

Then create python file like this

```python
import crazyimports
import config

print(config.number)
```

All top level properties from TOML file stored in attributes of a imported module

TOML files should have `.toml` extension
