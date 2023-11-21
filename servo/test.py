import servo_lib        

servo = servo_lib.servo(0)

while True:
    servo.goto(180)
    servo.wait()
    servo.goto(0)
    servo.wait()
