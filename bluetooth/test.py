import bluetooth
import bluetooth_lib #this library was modified from code written by MakeUseOf.

ble = bluetooth.BLE()
p = bluetooth_lib.BLESimplePeripheral(ble,"raspberry pi pico W")

def on_rx(v):
    print("RX", v[5:-1])
    p.send(v)

p.on_write(on_rx)