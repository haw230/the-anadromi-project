#### Make markdown files open link in new tab
```a target="_blank" href="http://some_other_site.com">Some Other site</a>``` does not work.

#### PyTest collecting 0 items and error 5 [Solved]
The function that has ```assert()``` must be named ```test_something```

#### Making Github folders [Solved]
Just type '/' at the end of name when making a file.

#### Python not finding modules [Solved]
* Remember to have the ```__init__.py``` file
* Make sure path is included in PYTHONPATH
* Python only searches what is in PYTHONPATH (sys.path), meaning that parent directories are ignored

```python
import sys

print(sys.path) #prints out all module search paths
sys.path.insert(0, '/path/to/file') #adds path to the front(in case of duplicates checked before
```
Use `print(sys.path)` to check whether or not the right paths are there, then use `sys.insert(0, '/path/to/file')` to add the path.
