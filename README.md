## Information

[![PyPI](https://img.shields.io/pypi/v/pylpchanged.svg)](https://pypi.org/project/pylpchanged)
[![PyPI](https://img.shields.io/pypi/format/pylpchanged.svg)]()
[![PyPI](https://img.shields.io/pypi/pyversions/pylpchanged.svg)]()

**pylpchanged** is a plugin for [Pylp](https://github.com/pylp/pylp) that filter unchanged
files.

**Note**: this plugin cannot filter unchanged files with a name transformed by another plugin
further into the stream (`pylprename` for example).


## Installation

Install **pylpchanged** with `pip`:

    pip install pylpchanged

If you don't have Python `Scripts` folder in your PATH you can run also:

    python -m pip install pylpchanged


## Usage

The usual use of **pylpchanged** is as follows:

```python
import pylp
from pylpchanged import changed

pylp.task('default', lambda:
    pylp.src('lib/*.py')
      .pipe(changed())
    # .pipe(another_plugin())
      .pipe(pylp.dest('build'))
)
```

Without parameters, **pylpchanged** will wait for the destination stream (i.e. `pylp.dest`)
to compare the last result with the source files.

For a faster execution you can pass directly the destination path like this:

```python
import pylp
from pylpchanged import changed

pylp.task('default', lambda:
    pylp.src('lib/*.py')
      .pipe(changed('build'))
    # .pipe(another_plugin())
      .pipe(pylp.dest('build'))
)
```

In fact, your can make your task even faster by reading the files after filtering them:

```python
import pylp
from pylpchanged import changed

pylp.task('default', lambda:
    pylp.src('lib/*.py', read=False)
      .pipe(changed('build'))
      .pipe(pylp.readnow())
    # .pipe(another_plugin())
      .pipe(pylp.dest('build'))
)
```
