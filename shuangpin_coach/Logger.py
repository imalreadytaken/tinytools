
class Logger:

    LOG_PATH = 'log.txt'
    ENCODING = 'utf-8'

    def __init__(self):
        self.handler = open(self.LOG_PATH,'a+',encoding=self.ENCODING)

    def log(self, content):
        self.handler.write(content + "\n")
        self.handler.flush()

    def close(self):
        self.handler.close()

