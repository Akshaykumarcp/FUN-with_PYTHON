## Logging in Python

#### CREDITS: https://docs.python.org/3/howto/logging-cookbook.html
---

### Why do we do logging?
- Logging is an important part of coding process to keep a track of all the events happening when the code is run. 
- By logging we can create custom messages/events to indicate different stages of the code. 
- Logging makes it easier to monitor , troubleshoot and debug the code.

---

- The most simple way of doing logging is using a "print" function. 
- But there are many disadvantages of using a "print" function and also there are many functionalities available with 
        "logger" method in python. 
- "Print" statement might let you debug the code in the case of error while the code is in development stage 
        but once you deploy the code to production, using logger is the best practice.

---

Logger provides different severity levels (warning, errors, critical, info etc.) to log different events. 
        As per the official python document, below are the different severity levels and their description:

1) DEBUG - Detailed information, typically of interest only when diagnosing problems.

2) INFO - Confirmation that things are working as expected.

3) WARNING - An indication that something unexpected happened, or indicative of some problem in the near 
            future (e.g. ‘disk space low’). The software is still working as expected.

4) ERROR - Due to a more serious problem, the software has not been able to perform some function.

5) CRITICAL - A serious error, indicating that the program itself may be unable to continue running.
