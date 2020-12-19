# YAML

Create file with the name `config.yaml`

```yaml
number: 42
```

Then create python file like this

```python
import crazyimports
import config

print(config.number)
```

All top level properties from YAML file stored in attributes of a imported module

YAML files should have `.yaml` or `.yml` extensions
