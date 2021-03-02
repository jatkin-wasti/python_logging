# Logging with Python
- There is an in built logging module that we can make use of
## Severity Levels
 **DEBUG**
 -

 **INFO**
 -

 **WARNING**
 -

 **ERROR**
 -

 **CRITICAL**
 -

### Module's Output
- If we run the following code from our py file
```
# Logging a message from each level
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```  
- We get the following output
![logging](images/logging_output.PNG)
- 'root' is the name that the logging module gives to it's default logger
- Format is 'level:name:message'
- By default, the logging module only logs messages that are of Warning level or
 higher (though this can be edited if you wish)
    - This can be done with the `basicConfig(**kwargs)` method
#### Basic Configurations
- We briefly mentioned the `basicConfig(**kwargs)` method but we'll dive deeper
into the parameters it takes
- level: set the root logger to this security level
- filename: specify the file
- filemode: file is opened in this mode (default is a for append)
- format: the format of the log message
