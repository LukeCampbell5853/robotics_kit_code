from time import sleep
from _thread import start_new_thread
from machine import Pin, PWM

class servo:
    def __init__(self,pin):
        self.pos = 0
        self.pin = PWM(Pin(pin))
        self.pin.freq(50)
        self.loc = 0
        self.moving = False
    
    def goto(self,pos):
        self.loc = int(1000+(pos/180)*8000)
        self.moving = True
        if self.pos < self.loc:
            steps = range(self.pos,self.loc,50)
        else:
            steps = range(self.pos,self.loc,-50)
        start_new_thread(self.rotate,(tuple(steps),))
    
    def rotate(self,steps):
        for step in steps:
            self.pin.duty_u16(step)
            sleep(0.01)
            self.pos = step
            if self.pos == self.loc-50 or self.pos == self.loc+50:
                self.moving = False
                break
    
    def wait(self):
        while self.moving:
            pass
