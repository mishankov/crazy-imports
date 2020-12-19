# JSON

Create file with the name `config.json`

```json
{
    "number": 42
}
```

Then create python file like this

```python
import crazyimports
import config

print(config.number)
```

All top level properties from JSON file stored in attributes of a imported module

JSON files should have `.json` extension
