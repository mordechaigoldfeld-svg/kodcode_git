import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter=logging.Formatter('%(levelname)s | %(asctime)s | %(message)s ')

stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter)

file_handler=logging.FileHandler('system.log',encoding='utf8')
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

