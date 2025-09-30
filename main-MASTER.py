from machine import Pin, UART
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

last_state = 0

while True:
    current_state = button.value()
    if current_state != last_state:
        if current_state == 1:
            print("Tlačítko stisknuto, posílám '1'")
            uart.write(b'1')
        else:
            print("Tlačítko puštěno, posílám '0'")
            uart.write(b'0')
        last_state = current_state
    time.sleep(0.05)
