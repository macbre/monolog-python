import logging
import json
import time
import traceback

from logging.handlers import SysLogHandler, SYSLOG_UDP_PORT

from socket import gethostname


class MonologHandler(SysLogHandler):
    """
    Syslog handler with Monolog formatter

    @see https://docs.python.org/2/library/logging.handlers.html#sysloghandler
    @see https://docs.python.org/3.4/library/logging.handlers.html#logging.handlers.SysLogHandler
    """
    def __init__(self, address=('localhost', SYSLOG_UDP_PORT)):
        super(MonologHandler, self).__init__(address)

        self.setFormatter(MonologFormatter())


class MonologFormatter(logging.Formatter):
    """
    JSON based logging formatter
    """
    converter = time.gmtime  # timestamps are in UTC zone

    def formatTime(self, record, datefmt=None):
        """
        https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-date-format.html#mapping-date-format

        yyyy-MM-dd'T'HH:mm:ss.SSS # date_hour_minute_second_millis

        :type record logging.LogRecord
        :type datefmt str
        :rtype: str
        """
        ct = self.converter(record.created)

        # @see https://docs.python.org/2/library/time.html#time.strftime
        t = time.strftime("%Y-%m-%dT%H:%M:%S", ct)
        s = "%s.%03d" % (t, record.msecs)
        return s

    def formatException(self, record):
        """
        Format and return the specified exception information as a string.

        :type record logging.LogRecord
        :rtype: dict
        """
        if record.exc_info is None:
            return {}

        (exc_type, exc_message, trace) = record.exc_info

        return {
            'exception': {
                'class': exc_type.__name__,  # ZeroDivisionError
                'message': str(exc_message),  # integer division or modulo by zero
                'trace': list(traceback.format_tb(trace)),
            }
        }

    def format(self, record):
        """
        :type record logging.LogRecord
        :rtype: str
        """
        context = dict(record.__dict__.get('context', {}))

        # add exception details (if any)
        context.update(self.formatException(record))

        # syslog expects ident string to be present
        ident = 'monolog[%d]: ' % record.process

        return ident + json.dumps({
            "@timestamp": self.formatTime(record),
            "@message": record.getMessage(),
            "@context": context,
            "@fields": {
                "filename": record.filename,
                "lineno": int(record.lineno),
            },
            "severity": str(record.levelname).lower(),
            "program": record.name,
            "@source_host": gethostname()
        }, separators=(',', ':'), sort_keys=True)
