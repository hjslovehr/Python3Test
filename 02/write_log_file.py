import logging

# 创建和配置日志
LOG_FORMAT = "[%(levelname)s] [%(asctime)s] %(message)s"
logging.basicConfig(filename=r".\test-log.txt", \
                    level=logging.DEBUG,\
                    format=LOG_FORMAT)
logger = logging.getLogger()

# 写日志
logger.info("Test log message")
