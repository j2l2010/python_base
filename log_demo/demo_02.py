import logging
import logging.handlers
import datetime


# 定义logger
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

# 定义handler
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# 给logger添加handler
logger.addHandler(rf_handler)
logger.addHandler(f_handler)


logger.debug(">>>> This is a debug log.")
logger.info(">>>> This is a info log.")
logger.warning(">>>> This is a warning log.")
logger.error(">>>> This is a error log.")
logger.critical(">>>> This is a critical log.")


