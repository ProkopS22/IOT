from machine import ADC
import utime

adc = ADC(26)

VREF = 3.3
ADC_RES = 65535 

while True:
    raw_value = adc.read_u16()
    voltage = (raw_value / ADC_RES) * VREF

    print("ADC hodnota:", raw_value, "| Napětí: {:.3f} V".format(voltage))

    utime.sleep(0.2) 
