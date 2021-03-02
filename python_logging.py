import logging # We need to import the logging module to use it in our file

# Changing the configuration to show all of the messages
#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.warning('This will get logged to a file')
#logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s-%(asctime)s')

# Logging a message from each level
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Logging a message with a variable
name = 'Jamie'
logging.error(f'{name} raised an error')

# Creating our own logger
logger = logging.getLogger('example_logger')
logger.warning('This is a warning')
