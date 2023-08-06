# Introduction 
This is a project to expose some of the utility tools used by givvable for easy version and use in projects throughout ouur code.

## DB
Helps connect to postgresql DB

```python3
import db
db.get_conn('stage-postgresql')
```

# Developing
To install givvableutils, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
pip install -e .[dev]
python3 setup.py bdist_wheel
python3 setup.py sdist
twine upload --skip-existing dist/*
```