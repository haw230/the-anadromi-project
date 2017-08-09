#### Have markdown files open link in new tab
```a target="_blank" href="http://some_other_site.com">Some Other site</a>``` does not work. Whatever, this is a minor problem.

#### Python complex data structures [Solved]
Unlike simple data strucutures such as strings or numbers, Python, similar to many languages, stores a reference for lists instead of its actual value. By calling two functions (user-written and solved) with the same list as a parameter, they ended up as the same value because they both reference the same list. The solution is to create a separate list using ```list(ls)```, creating a new list with a new reference.  

#### Makefile can't find the file ```python: can't open file 'main.py': [Errno 2] No such file or directory``` [Solved]
The Makefil couldn't find main.py even though I ```cd```'d to the right directory. Apparently in Makfiles, ```cd``` is only effective for that one line which means by the time ```python main.py``` ran, it was in the original directory again which did not have the file. Solution is to use ```cd selection_sort/ && python main.py```.

#### Makefile error ```make: *** No rule to make target `test'.  Stop.``` [Solved]
In the wrong directory. ```ls Makefile``` to make sure the file is there, if not, just ```cd``` to the right directory.

#### PyTest collecting 0 items and error 5 [Solved]
The function that has ```assert()``` must be named ```test_something```

#### PyTest acting up again [Solved]
Gotta install this ```six``` module. Don't know how/why it got uninstalled but threw that into ```dev-requirements.txt``` just in case.

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

#### Can't open Anaconda [Solved]
[StackOverflow](https://stackoverflow.com/questions/18675907/how-to-run-conda). Basically, just run ```export PATH=~/anaconda3/bin:$PATH```, the number following anaconda is your version number. Then, all the ```conda``` commands will work.

#### Installing Anaconda on Linux [Solved]

Follow the [tutorial](https://docs.continuum.io/anaconda/install/linux)
