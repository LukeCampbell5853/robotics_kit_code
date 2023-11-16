import oled_lib
import icons
from machine import Pin, I2C

OLED_i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)#pi pico only has a certain number of pins avaliable
screen = oled.SSD1306_I2C(128, 64, OLED_i2c, addr=0x3c)

screen.fill(0)#fill entire screen, 0 is for black, 1 is for white

def display(element):
    for x,y in element:
        screen.pixel(x,y,1)

display(icons.background)
display(icons.auto)
display(icons.back)
display(icons.no_conn)

screen.show()