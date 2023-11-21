from machine import Pin
from utime import sleep

red_led = Pin(0, Pin.OUT)

red_led.high()

while True:
  sleep(1)
  red_led.toggle()
