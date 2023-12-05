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
