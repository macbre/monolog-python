# monolog-python
Python's logging formatter compatible with monolog-utils

## Example

```python
import logging
from monolog import MonologHandler


def fun():
    return 2/0


logger = logging.getLogger('monolog.example')
logger.addHandler(MonologHandler())  # send message to a local syslog

try:
    fun()
except ZeroDivisionError:
    logger.error('fun() call raised an exception', exc_info=True)
```

```
$ python monolog/examples/example.py
```

```json
{
  "@context": {
    "exception": {
      "class": "ZeroDivisionError",
      "message": "integer division or modulo by zero",
      "trace": [
        "  File \"monolog/examples/example.py\", line 32, in <module>\n    fun()\n",
        "  File \"monolog/examples/example.py\", line 7, in fun\n    return 2/0\n"
      ]
    }
  },
  "@fields": {
    "filename": "example.py",
    "lineno": 34
  },
  "@message": "fun() call raised an exception",
  "@source_host": "debian",
  "@timestamp": "2016-01-02T22:45:33.336",
  "program": "monolog.example",
  "severity": "error"
}
```
