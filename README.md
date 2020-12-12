# SimpleCsv

This package is built to make it truly simple to open an work with a standard CSV file. It was initially written so that students who have just learned python can get started with data as early as possible. 

```python
from simplecsv import SimpleCsv

def main():
    data = SimpleCsv('test.csv')
    for datum in data:
        print(datum)
```
