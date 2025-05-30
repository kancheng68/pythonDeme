"""
记录日志和设置
"""
import logging


logging.getLogger('logger_test')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='../logging_docs/logger_test.log')
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
