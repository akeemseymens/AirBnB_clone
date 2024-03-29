# AirBnB clone - The console

<p align="center">
    <img src="https://i.imgur.com/JOhaZ5m.png">
</p>

## Description

This team project is part of the Holberton School Full-Stack Software Engineer program.
It's the first step towards building a first full web application: an AirBnB clone.
This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.
* All code was created on ```Python 3.4``` or greater.
* Python stylecode format with [```PEP8```](https://www.python.org/dev/peps/pep-0008/)


## Learning Objectives

 * How to create a Python package
 * How to create a command interpreter in Python using the cmd module
 * What is Unit testing and how to implement it in a large project
 * How to serialize and deserialize a Class
 * How to write and read a JSON file
 * How to manage datetime
 * What is an ```UUID```
 * What is ```*args``` and how to use it
 * What is ```**kwargs``` and how to use it
 * How to handle named arguments in a function

## Console and Command Usage

The console is a Python shell-like command line user interface provided by the python [CmdModule](https://wiki.python.org/moin/CmdModule)
It prints a prompt and waits for the user for input, for our project we used **(hbnb)** 

Command | Example
------- | -------
Display commands help | ```(hbnb) help <command>```
Create object (prints its id)| ```(hbnb) create <class>```
Destroy object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Show "all" objects or instances class | ```(hbnb) all``` or ```(hbnb) all <class>```
Run console | ```./console.py```
Quit console | ```(hbnb) quit```


Help command example

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

## Class Models Used


File | Description | Attributes
---- | ----------- | ----------
[base_model.py](./models/base_model.py) | The BaseModel class is inherited by other classes | id, created_at, updated_at
[user.py](./models/user.py) | User class stores user-related info | email, password, first_name, last_name
[city.py](./models/city.py) | City class stores city-specific information | state_id, name
[state.py](./models/state.py) | State class stores state-specific information | name
[place.py](./models/place.py) | Place class stores full detailed outline of rental unit features | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
[review.py](./models/review.py) | Review class stores previous customer reviews and opinions | place_id, user_id, text
[amenity.py](./models/amenity.py) | Amenity class stores highlighted amenity information | name

## Tests

All the code is tested with the [unittest module](https://docs.python.org/3/library/unittest.html).
The test for the classes are in the [test_models](./tests/test_models/) folder.

## Authors

* **Akeem Seymens** - [812@holbertonschool.com](https://github.com/akeemseymens)
* **Edward Guillermo** - [803@holbertonschool.com](https://github.com/<ed>)
