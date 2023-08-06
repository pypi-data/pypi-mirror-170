![test-badge](https://github.com/danielschweigert/pypgsync/actions/workflows/lint-and-test.yml/badge.svg)

[//]: # (![coverage-badge]&#40;https://raw.githubusercontent.com/danielschweigert/pypgsync/main/coverage-manual.svg&#41;)

# pypgsync
Python utility to sync two postgresql databases


## Installation

```bash
pip install pypgsync
```

## Usage
With the goal to synchronize a destination database to the state of a source database, whereas the 
source database grows in append-only fashion (no updates), the following steps can be run using 
pypgsync:
```python
import psycopg
from pypgsync.pypgsync import sync

con_source = psycopg.connect(host="host_source", 
                             dbname="db_source", 
                             user="user_source", 
                             password="secret_source")
cur_source = con_source.cursor()

con_destination = psycopg.connect(host="host_destination", 
                                  dbname="db_destination", 
                                  user="user_destination", 
                                  password="secret_destination")

sync(cur_source, con_destination, tables=["table_a", "table_b", "table_c"], chunk_size=100)
```