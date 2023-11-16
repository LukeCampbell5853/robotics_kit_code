import servo_lib        

servo1 = servo_lib.servo(0)

while True:
    servo1.goto(180)
    servo1.wait()
    servo1.goto(0)
    servo1.wait()