# JavaDoc2HTML

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/3f9a6627b48841e9ae2fcc4d4743ec33)](https://app.codacy.com/gh/Moultree/javadoc2html/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)  

Author: Nikolay Tikhonchik (`okaykudes@gmail.com`)

## About  
This is a simple Python utility that parses JavaDoc from given Java files and generates HTML view from it.  
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

## Tasks

During my work on this project, I was givan a handful of tasks to implement:  

- [x] Test coverage `80%`  
- [x] Specifying parent classes for derived classes  
- [x] Specifying function prototypes  
- [x] Inner links (`@link`, `@see`)  
- [x] Ability to change color scheme  
- [x] Ability to change logos    

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
