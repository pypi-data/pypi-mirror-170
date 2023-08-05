# PySimpleTest -- Make test as simple as possible

PySimpleTest is a very simple test framwork. To start using it, try following example:  
Write a file `main.py`:

```python
from PySimpleTest import *

a = 2
should_be_equal(a, 2)
should_be_less(a, 1)
```

Then run it. You can get following cmd output:

![avatar](https://gitee.com/time-coder/PySimpleTest/raw/master/images/first_example.png)

Please see full documentation at [https://github.com/Time-Coder/PySimpleTest](https://github.com/Time-Coder/PySimpleTest)

## Release Note
### 1.0.7
* Fix issue #1: `should_be_true` works fine now;
* Fix issue #2: `PySimpleTest` can run on `Linux` and `Mac` now.
### 1.0.6
* Don't need `enable(enhance_func)` any more;
* Fix "exit code not working" bug.
### 1.0.5
* Added `Section` class. User can use `Section` with Python `with` syntax instead of `section`, `end_section`, `subsection`.
### 1.0.2
* First release for all basic functions.