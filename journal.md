## Friday July 21
Started working on actual lessons. Will figure out tests later.

## Monday July 24
Weird error bugged me all morning with pytest. Apparently test function names must be start with ```test_``` such as 
``` python
def test_simple():
    assert(1) = 1
```
Otherwise pytest won't work. Understood makefiles better today. --verbose and --disable-pytest-warnings are useful. There are other flags too. Got tests to continue after failure.
