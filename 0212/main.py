from multiprocessing import Process, Lock
from random import randint
from time import sleep

class Philosopher(Process):
    EAT_TIME = (1, 3)
    TIMEOUT = 10
    THINK = (3, 5)
    def __init__(self, name, r_cs, l_cs):
        super().__init__()
        self.name = name
        self.r_cs = r_cs
        self.l_cs = l_cs
    
    def eat(self):
        print('Философ {} ест'.format(self.name))
        sleep(randint(*Philosopher.EAT_TIME))
        print('Философ {} поел и положил палочки'.format(self.name))
        
    def run(self):
        while True:
            r_ac = self.r_cs.acquire(timeout=Philosopher.TIMEOUT)
            if r_ac:
                print('Философ {} взял правую палочку'.format(self.name))
                l_ac = self.l_cs.acquire(timeout=Philosopher.TIMEOUT)
                if l_ac:
                    print('Философ {} взял левую палочку'.format(self.name))

                if l_ac and r_ac:
                    self.eat()
                    print('Философ {} думает'.format(self.name))
                    self.r_cs.release()
                    self.l_cs.release()
                    sleep(randint(*Philosopher.THINK))
                    print('Философ {} прекратил думать, т.к. проголодался'.format(self.name))
                else:
                    print('Философ {} думает'.format(self.name))
            
PHILOSOPHERS = 5
    
if __name__ == '__main__':
    chpstck = [Lock() for _ in range(PHILOSOPHERS)]
    for j in range(PHILOSOPHERS):
        print('Философ {} думает'.format(j))    
    for i in range(PHILOSOPHERS):
        r_cs = chpstck[i]
        l_cs = chpstck[i-1]
        Philosopher(str(i), r_cs, l_cs).start()
        