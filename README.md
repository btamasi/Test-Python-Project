# Test Python Project

## Using the skeleton

- Copy skeleton to the project folder
- Rename `NAME` directory to the name of the project
- Edit `setup.py`.
- Rename `tests/NAME_tests.py` by replacing `NAME` to the project directory name
- Replace in `tests/NAME_tests.py` `NAME` to the name of the project
- Use `nosetests` to check it
- Add code to the in the *module directory*
- Add scripts to `bin/`
- Add script names to `setup.py`
- Check for errors with `nosetests`
- Use `python setup.py sdist` to create a source distribution for the *module*
- (Add `dist/`, `*.egg-info`, and `*.pyc` to `.gitignore`)

## Installation

To install **testproj** module use `python setup.py install`.
To uninstall it use **pip**: `pip uninstall testproj`.

## Usage

To run the **script**: Just type `script1.py`.
To use the **module**: In Python, use

```
from testproj import printtest as pt
pt.printtest("foo")
```

## References

Zed Shaw's [Learn Python the Hard Way](http://learnpythonthehardway.org/book/ex46.html).

