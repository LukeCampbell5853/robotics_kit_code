import sensor_lib
import utime

sensor = sensor_lib.sensor(15,14)

while True:
    print("dist:" + str(sensor.measure()))
    utime.sleep(1)
