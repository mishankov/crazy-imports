# CSV

Create file with the name `example_table.csv`

```csv
1,23,34,23
apple, orange, pineapple, grape
```

Then create python file like this

```python
import crazyimports
import example_table

for row in example_table.data:
    print(", ".join(row))
```

Rows of CSV files stored in a list `<file_name>.data`

CSV files should have `.csv` extension
