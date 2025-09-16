from machine import ADC, Pin, PWM
import utime

# --- Nastavení ADC (fotoresistor na GP26) ---
ldr = ADC(26)

# --- Nastavení LED (PWM na GP15) ---
led_pin = Pin(15)
led_pwm = PWM(led_pin)
led_pwm.freq(1000)   # frekvence PWM 1 kHz

# --- Kalibrační proměnné (můžeš upravit podle podmínek) ---
VREF = 3.3
ADC_MIN = 0       # nejnižší hodnota (úplná tma)
ADC_MAX = 65535   # nejvyšší hodnota (plné světlo)

while True:
    # Čtení světla
    light_val = ldr.read_u16()  # 0–65535
    
    # Inverzní jas (méně světla → vyšší duty)
    duty = 65535 - light_val
    
    # Oříznutí do rozsahu
    if duty < 0:
        duty = 0
    if duty > 65535:
        duty = 65535
    
    # Nastavení PWM
    led_pwm.duty_u16(duty)
    
    print("Světlo:", light_val, "| Jas LED (duty):", duty)
    utime.sleep(0.1)
