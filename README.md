# Coding-style


Setting up development Environment on Linux
----------------------------------

### Install Project (edit mode)

#### Working copy
    
    $ cd /path/to/workspace
    $ cd coding-style
    $ pip install -e .
 
### Setup Database

#### Configuration

```yaml

db:
  url: postgresql://postgres:postgres@localhost/coding-style_dev
  test_url: postgresql://postgres:postgres@localhost/coding-style_test
  administrative_url: postgresql://postgres:postgres@localhost/postgres
```

#### Remove old abd create a new database **TAKE CARE ABOUT USING THAT**

    $ coding-style db create --drop --mockup

And or

    $ coding-style db create --drop --basedata 

#### Drop old database: **TAKE CARE ABOUT USING THAT**

    $ coding-style [-c path/to/config.yml] db --drop

#### Create database

    $ coding-style [-c path/to/config.yml] db --create

Or, you can add `--drop` to drop the previously created database: **TAKE CARE ABOUT USING THAT**

    $ coding-style [-c path/to/config.yml] db create --drop


### Running tests

```bash
pip install -r requirements-dev.txt
pytest
```

### Running server

#### Single threaded 

```bash
coding-style [-c path/to/config.yml] serve
```

#### WSGI

wsgi.py

```python
from coding-style import coding-style
coding-style.configure(files=...)
app = coding-style
```

```bash
gunicorn wsgi:app
```

### How to start

Checkout `coding-style/controllers/foo.py`, 
`coding-style/models/foo.py` and `coding-style/tests/test_foo.py` to
learn how to create an entity.

