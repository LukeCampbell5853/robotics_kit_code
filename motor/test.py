from motor_lib import motor
from time import sleep

motor1 = motor(0,1)
            
while True:
    for speed in range(-100,100,1):
        motor1.speed(speed)
        sleep(0.01)
    for speed in range(100,-100,-1):
        motor1.speed(speed)
        sleep(0.01)
