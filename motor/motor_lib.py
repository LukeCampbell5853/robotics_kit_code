from machine import Pin, PWM

class motor:
    def __init__(self,p1,p2):
        self.__p1 = PWM(Pin(p1))
        self.__p2 = PWM(Pin(p2))
        self.__p1.freq(1000)
        self.__p2.freq(1000)
        self.__p1.duty_u16(0)
        self.__p2.duty_u16(0)
        self.__signal = 0
    
    def speed(self,speed):
        self.__signal = abs(int((speed/100)*65025))
        if speed > 0:
            self.__p1.duty_u16(0)
            self.__p2.duty_u16(self.__signal)
        else:
            self.__p2.duty_u16(0)
            self.__p1.duty_u16(self.__signal)
