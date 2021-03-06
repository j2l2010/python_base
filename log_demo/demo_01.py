import logging

LOG_FORMAT = '%(asctime)s====%(levelname)s+++++%(message)s'
logging.basicConfig(filename="log_demo.log", level=logging.DEBUG, format=LOG_FORMAT)

logging.debug(">>>> This is a debug log.")
logging.info(">>>> This is a info log.")
logging.warning(">>>> This is a warning log.")
logging.error(">>>> This is a error log.")
logging.critical(">>>> This is a critical log.")


logging.log(logging.DEBUG, ">>>> This is a debug log.")
logging.log(logging.INFO, ">>>> This is a info log.")
logging.log(logging.WARNING, ">>>> This is a warning log.")
logging.log(logging.ERROR, ">>>> This is a error log.")
logging.log(logging.CRITICAL, ">>>> This is a critical log.")

# 因为没有配置日志，默认输出结果只显示warning以上级别的日志
