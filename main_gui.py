import serial
import threading
import tkinter as tk
import time

led_pico = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
button_pico = serial.Serial('/dev/ttyACM1', 115200, timeout=1)

def read_button():
    while True:
        line = button_pico.readline().decode().strip()
        if line == "BUTTON_PRESSED":
            toggle_led()

def led_on():
    led_pico.write(b"LED_ON\n")
    led_Label.config(text="LED: ON", fg="green")
    
def led_off():
    led_pico.write(b"LED_OFF\n")
    led_Label.config(text="LED: OFF", fg="red")
    
def toggle_led():
    current = led_Label.cget("text")
    if "OFF" in current:
        led_on()
    else:
        led_off()
        
root = tk.Tk()
root.title("oládání LED")
root.geometry("250x180")

led_Label = tk.Label(root, text="LED: OFF", font=("Arial", 16), fg="red")
led_Label.pack(pady=10)

on_button = tk.Button(root, text="Rozsvítit LED", width=15, command=led_on)
on_button.pack(pady=5)

off_button = tk.Button(root, text="zhasnout LED", width=15, command=led_off)
off_button.pack(pady=5)

thread = threading.Thread(target=read_button, daemon=True)
thread.start()

root.mainloop()