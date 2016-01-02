import logging

from monolog import MonologFormatter, MonologHandler


def fun():
    return 2/0


logging.basicConfig(
    level=logging.DEBUG
)

logger = logging.getLogger('monolog.example')

# emit JSON-formatted message to stdout
handler = logging.StreamHandler()
handler.setFormatter(MonologFormatter())

logger.addHandler(handler)

# and send to local syslog
logger.addHandler(MonologHandler())
#logger.addHandler(MonologHandler(address=('x.x.x.x', 59514)))

logger.debug('Debug msg')
logger.info('Foo')
logger.warning('Foo with context', extra={'context': {'foo': 42, 'bar': True}})


try:
    fun()
except ZeroDivisionError:
    logger.error('fun() call raised an exception', exc_info=True, extra={'context': {'foo': 3}})


"""
[2016-01-02 22:08:44,948][DEBUG][action.index             ] [Amiko Kobayashi] [syslog-ng_2016-01-02][4], node[UMAtc3QtQDOW8i6ynkmcUw], [P], v[2], s[STARTED], a[id=GFtTwGlXSl2wipjNnXtlAw]: Failed to execute [index {[syslog-ng_2016-01-02][syslog][AVIEYrmTbEun8bxLbMei],
source[{},"@fields":{"filename":"example.py","lineno":26},"@message":"Debug msg","@source_host":"debian","@timestamp":"2016-01-02T22:08:47.000295Z","program":"monolog.example","severity":"debug"}
]}]

{"@context":{},"@fields":{"filename":"example.py","lineno":26},"@message":"Debug msg","@source_host":"debian","@timestamp":"2016-01-02T22:08:33.000335Z","program":"monolog.example","severity":"debug"}

"""