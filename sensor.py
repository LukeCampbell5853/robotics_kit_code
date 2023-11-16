from machine import Pin
import utime
   
class sensor:
    def __init__(self,trig,echo):
        self.trigger = Pin(trig, Pin.OUT)
        self.echo = Pin(echo, Pin.IN)
    
    def measure(self):
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()
        while self.echo.value() == 0:
            signaloff = utime.ticks_us()
        while self.echo.value() == 1:
            signalon = utime.ticks_us()
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        return(distance)