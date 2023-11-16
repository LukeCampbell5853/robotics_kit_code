from machine import Pin, PWM
from utime import sleep

class motor:
    def __init__(self,pin1,pin2):
        self.__pin1 = PWM(Pin(pin1))
        self.__pin2 = PWM(Pin(pin2))
        self.__signal = 0
    
    def set_speed(self,speed):
        self.__signal = int((speed/100)*65025)
        if speed > 0:
            self.__pin1.duty_u16(0)
            self.__pin2.duty_u16(self.__signal)
        else:
            self.__pin2.duty_u16(0)
            self.__pin1.duty_u16(self.__signal)
