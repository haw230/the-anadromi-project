#### Making Github folders [Solved]
Just type '/' at the end of name when making a file.

#### Python not finding modules [Solved]
* Remember to have the ```__init__.py``` file
* Remember to have the right path
* Python only searches what is in PYTHONPATH (sys.path), so their parent directories are ignored

```python
import sys

print(sys.path) #prints out all module search paths
sys.path.insert(0, '/path/to/file')
```
Use `print(sys.path)` to check whether or not the right paths are there, then use `sys.insert(0, '/path/to/file')` to add the path.
