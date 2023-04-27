# JavaDoc2HTML

Author: Nikolay Tikhonchik (`okaykudes@gmail.com`)

## About  
This is a simple Python utility that parses JavaDoc from given Java files and geenerates HTML view from it.  
It can be used as intended or as a reference solution.

## Features
- Easy-to-use command line interface.
- Neat design.
- Ability to parse whole directory.

## Requirements 
- Python >3.10
- Jinja2

## Installation

To install, run the following commands:
```
pip install -r requirements.txt
```

## Usage

```
python -m javadoctohtml directory
python -m javadoctohtml path/to/file.java
```

## Structure

- App runner: `javadoctohtml.py`  
- Regex patterns: `pattern.py`  
- Java parser: `parse.py`  
- Java definitions as Python objects: `objects.py`  

## Testing

At this moment, test coverage for this project is `97%`.  
You can see all tests in the `/tests` directory.  

| Name            | Stmts | Miss | Cover |
|-----------------|-------|------|-------|
|javadoctohtml.py |    43 |    4 |   91% |
|objects.py       |    68 |    5 |   93% |
|parse.py         |   151 |    0 |  100% |
|pattern.py       |     8 |    0 |  100% |

## License

This project is licensed under the [MIT license](LICENSE).