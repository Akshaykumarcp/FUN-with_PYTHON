""" 
CREDITS: https://docs.python.org/3/howto/logging-cookbook.html

Logging in Python

Why do we do logging?
- Logging is an important part of coding process to keep a track of all the events happening when the code is run. 
- By logging we can create custom messages/events to indicate different stages of the code. 
- Logging makes it easier to monitor , troubleshoot and debug the code.

- The most simple way of doing logging is using a "print" function. 
- But there are many disadvantages of using a "print" function and also there are many functionalities available with 
        "logger" method in python. 
- "Print" statement might let you debug the code in the case of error while the code is in development stage 
        but once you deploy the code to production, using logger is the best practice.

Logger provides different severity levels (warning, errors, critical, info etc.) to log different events. 
        As per the official python document, below are the different severity levels and their description:

1) DEBUG - Detailed information, typically of interest only when diagnosing problems.

2) INFO - Confirmation that things are working as expected.

3) WARNING - An indication that something unexpected happened, or indicative of some problem in the near 
            future (e.g. ‘disk space low’). The software is still working as expected.

4) ERROR - Due to a more serious problem, the software has not been able to perform some function.

5) CRITICAL - A serious error, indicating that the program itself may be unable to continue running.

Let's see how we can use Logging method in python.
"""

# import logging python module
import logging

# let's create a log file with name "logger" and set the severity level to "info"
logging.basicConfig(filename='logging/Logger1.log',level=logging.INFO)
logging.info("Info message ")
logging.warning("Warning message")
logging.error("Error message")

# Let's open the log file created and see if the messages are logged.

logging.shutdown()

# add timestamps to  logs

logging.basicConfig(filename='logging/logger2.log',level=logging.INFO, format='%(asctime)s %(message)s') 

""" logging.basicConfig(filename='logging/logger2.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S') """
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message!!")

logging.shutdown()

logging.basicConfig(filename='logging/main.log',level=logging.INFO, 
                    format='%(asctime)s %(message)s') # here we have set our default level to info, so all levels after info will be displayed.
def divideNum(a,b):
    logging.info("Numbers are %s and %s", a,b) # Logging variables
    try:
        div = a/b
        logging.info("Method completed!!")
        return div
    except Exception as e:
        print("Check logs for exception!")
        logging.error("Error occured!!")
        logging.exception("Exception occured : " + (str(e)))
        
    
divideNum(4,2)
2.0
divideNum(4,0)
# have a look at the log file for exception


logging.shutdown()

# Lets check different log level messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

""" 
- This shows the log level before each message along side root, which is the name the logging module provides for its 
      default logging. 
      This configuration, which shows the level, name, and message isolated by a colon (:), is the default format.

- Notice:- debug() and info() messages didn't get logged. This is on the grounds that, as a matter of course, 
      the logging module logs the messages with a seriousness level of WARNING or above. 
      You can change that by designing the logging module to log occasions everything being equal on the off chance 
          that you need.

Capturing Stack Traces
- The logging module allows you to capture the full stack exception info and exception infor can be logged if the 
    exc_info is passed as True in argument. Let us check below information.
 """

# Trying to open the file which doesn't exist and log file not found exception in looger file.
import logging

try:
  with open("file.csv","r"):
    print("file read")
except Exception as e:
  logging.error("Exception occurred", exc_info=True)

#Now, we can check same example without exc_info
import logging

try:
  logging.info("Example started without using exc_info")
  with open("file.csv","r"):
    print("file read")
except Exception as e:
  logging.error("Exception occurred")

""" 

- Logging error with exc_info = true and logging_exception gives same result for logging an exception.

Logging to multiple destination
- Let’s say we want to log to console and file with different messages and in differing circumstances. 
- Say you want to log messages with levels of DEBUG and higher to file, and those messages at level INFO and higher 
    to the console. 
- Let’s also assume that the file should contain timestamps, but the console messages should not. 
- Here’s how you can achieve this:
 """
import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='logging/multiple.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console_log = logging.StreamHandler()
console_log.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console_log.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console_log)

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Logging to the root logger.')

# Now, define a couple of other loggers which might represent areas in your
# application:

logger1 = logging.getLogger('logger1.area1')
logger2 = logging.getLogger('logger2.area2')

logger1.debug('Hello, greetings.')
logger1.info('different domains.')
logger2.warning('This is a warning message.')
logger2.error('This is an error message.')
""" root        : INFO     Logging to the root logger.
root        : INFO     Logging to the root logger.
logger1.area1: INFO     different domains.
logger1.area1: INFO     different domains.
logger2.area2: WARNING  This is a warning message.
logger2.area2: WARNING  This is a warning message.
logger2.area2: ERROR    This is an error message.
logger2.area2: ERROR    This is an error message. """

""" Here we are consoling the output as well as we are logging in a file

CREDITS: https://docs.python.org/3/howto/logging-cookbook.html """

import logging
import math
logging.basicConfig(level=logging.INFO)

def sqrt(a):
    """Compute the square root"""
    return math.sqrt(a)

logging.info("square root of {a} is {b}".format(a=3, b=sqrt(3)))
# INFO:root:square root of 3 is 1.7320508075688772