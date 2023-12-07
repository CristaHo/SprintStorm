"""
This handles all of the logging in this project.
It is used by importing log from this file and
using log.info(<message>)/log.info(f"<message {with} fstring"), .debug, .warn and .error

The format will be [<time>]  <message's log level> - <message>
"""
import logging


# create logger
log = logging.getLogger('simple_example')
log.setLevel(logging.INFO)

# create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")

# add formatter and formatter to ch
ch.setFormatter(formatter)
log.addHandler(ch)
