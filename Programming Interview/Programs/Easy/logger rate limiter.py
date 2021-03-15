class Logger:
    def __init__(self):
        self.queue = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.queue:
            self.queue[message] = timestamp
            return True
        if timestamp - self.queue[message] > 9:
            self.queue[message] = timestamp
            return True
        else:
            return False


logger = Logger()
print (logger.shouldPrintMessage(1, "foo"))
print (logger.shouldPrintMessage(2,"bar"))
print (logger.shouldPrintMessage(3,"foo"))
print (logger.shouldPrintMessage(8,"bar"))
print (logger.shouldPrintMessage(10,"foo"))
print (logger.shouldPrintMessage(11,"foo"))