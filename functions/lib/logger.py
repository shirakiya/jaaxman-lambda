import logging


def get_logger():
    logger = logging.getLogger('functinos')
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(levelname)s] %(pathname)s:%(lineno)d: %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


logger = get_logger()
