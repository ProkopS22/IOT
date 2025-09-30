from machine import Pin, UART
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
led = Pin(15, Pin.OUT)

while True:
    if uart.any():
        print("Přijímám...")
        data = uart.read(1)
        if data == b'1':
            led.value(1)
            print("Přijato '1' — LED rozsvícena")
        elif data == b'0':
            led.value(0)
            print("Přijato '0' — LED zhasnuta")
        else:
            print("Přijato neznámé data:", data)
    time.sleep(0.05)
