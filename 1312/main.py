from threading import Thread, Condition, Lock
from random import randint, choice
from time import sleep

book = ''

class Writer(Thread):
    TIMEOUT = (1, 3)
    SLEEP = (1, 3)
    BOOK_LEN = 5
    def __init__(self, name):
        super().__init__()
        self.name = name
      
    def run(self):
        while True:
            global text
            lock.acquire()
            text = ''
            print('Писатель {} пишет книгу'.format(self.name))
            if not text:
                for _ in range(Writer.BOOK_LEN):
                    text += choice(list('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'))
                    sleep(randint(*Writer.TIMEOUT))
                    condition.acquire()
                    condition.notify_all()
                    condition.release()
            print('Писатель {} закончил писать книгу: {}'.format(self.name, text))
            lock.release()
            sleep(randint(*Writer.SLEEP))

class Reader(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global text
        while True:
            with condition:
                condition.wait()
                print("Читатель {} читает: {}".format(self.name, text))

WRITERS_AM = 5
READERS_AM = 10

if __name__ == "__main__":
    condition = Condition()
    lock = Lock()
    for writers in range(WRITERS_AM):
        Writer(str(writers)).start()
    for readers in range(READERS_AM):
            Reader(str(readers)).start() 
        