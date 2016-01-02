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
# logger.addHandler(MonologHandler(address=('x.x.x.x', 59514)))

logger.debug('Debug msg')
logger.info('Foo')
logger.warning('Foo with context', extra={'context': {'foo': 42, 'bar': True}})


try:
    fun()
except ZeroDivisionError:
    logger.error('fun() call raised an exception', exc_info=True, extra={'context': {'foo': 3}})
