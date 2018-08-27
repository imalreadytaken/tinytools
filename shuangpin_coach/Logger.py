
class Logger:

    LOG_PATH = './'
    LOG_FILE = '_log.txt'
    ENCODING = 'utf-8'

    def __init__(self, code):
        self.handler = open(self.LOG_PATH + code + self.LOG_FILE,'a+',encoding=self.ENCODING)

    def log(self, content):
        self.handler.write(content + "\n")
        self.handler.flush()

    def close(self):
        self.handler.close()


