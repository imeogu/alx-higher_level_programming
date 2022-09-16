# Python - Object-relational mapping
## Introduction
This project is all about linking Databases and Python.
In the first part, the module MySQLdb was used to connect to a MySQL database and execute your SQL queries.
In the second part, the module SQLAlchemy was used. It is an Object Relational Mapper (ORM).

## Requirements
- Ubuntu 20.04 LTS using node (version 14.x)
- The first line of all your files should be [#!/usr/bin/node]
- Files will be executed with MySQLdb version 2.0.x
- Files will be executed with SQLAlchemy version 1.4.x
- All files must be executable
## File Description
### Tasks
**[0-select_states.py](0-select_states.py)**
* Description:
    * Lists all states from the database hbtn_0e_0_usa
* Requirements:
    * Takes 3 arguments: `mysql username`, `mysql password` and `database name`

**[1-filter_states.py](1-filter_states.py)**
* Description:
    * Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
* Requirements:
    * Takes 3 arguments: `mysql username`, `mysql password` and `database name`

**[2-my_filter_states.py](2-my_filter_states.py)**
* Description:
    * Takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
* Requirements:
    * Takes 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched`