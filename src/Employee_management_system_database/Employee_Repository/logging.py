import logging

logging.basicConfig(
    filename = '../../logs/application.log',
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    filemode = 'w'
)
logger = logging.getLogger(__name__)
