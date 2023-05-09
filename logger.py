

import logging

logging.basicConfig(level=10,filename='demo.log',filemode='w',
                    format='%(asctime)s: %(levelname)s::%(message)s:',
                    datefmt="%d/%m/%Y %I:%M:%S")
logging.critical("critical message")
logging.error("error message")
logging.warning("warning message")
logging.info("info message")
logging.debug("debug message")
