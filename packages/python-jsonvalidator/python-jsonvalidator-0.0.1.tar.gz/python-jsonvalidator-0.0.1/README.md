
# Json Validator

A simple json validaor that validates a json object against a provided schema




## Features

- Validates a json object against a provided schema


## Tech Stack

Python3


## Installation

```bash
  pip3 install jsonvalidator
```

## Usage/Examples

```python
from jsonvalidator import jsonvalidator

schema = {
    "name": ["required", "string"],
    "phone": ["required", "string"],
    "email": ["required", "string"],
    "test": ["required", "boolean"],
    "job": {
        "title": ["required", "string"],
        "department": ["required", "string"],
        "salary": [
            {
                "gross": ["required", "float"],
                "net": ["required", "float"],
            },
        ],
    },
    "pet_names": ["required", "list"],
}

json_object = {
    "name": "John Doe",
    "phone": "+1 5555 5555",
    "email": "email",
    "test": True,
    "job": {
        "title": "Software Engineer",
        "department": "Engineering",
        "salary": [
            {
                "gross": 50000.00,
                "net": 50000.00,
            },
        ],
    },
    "pet_names": ["my pet"],
}


print(json_validator.validate_json(schema=schema, json_object=json_object)) # returns a json object
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@murungakibaara](https://www.github.com/murungakibaara)

