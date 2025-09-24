from machine import Pin, ADC
import time, math

# --- Hardware nastavení ---
pot = ADC(26)              # potenciometr na GP26 = ADC0
button = Pin(15, Pin.IN, Pin.PULL_UP)  # tlačítko s interním pull-up

# --- Pomocné funkce ---
def read_temperature():
    """
    Simulace teploty pomocí potenciometru:
    - ADC (0–65535) převedeme na 0–100 °C
    """
    raw = pot.read_u16()
    temp_c = (raw / 65535) * 100
    return round(temp_c, 1)

def wait_for_press():
    """
    Čekání na stisk tlačítka s debouncingem
    """
    while True:
        if button.value() == 0:   # stisk (protože pull-up)
            time.sleep_ms(20)     # debounce delay
            if button.value() == 0:
                while button.value() == 0:  # počkej na uvolnění
                    time.sleep_ms(10)
                return

def measure_statistics(n=5, delay=0.5):
    """
    Provede n měření s pauzou delay (s)
    a vrátí seznam hodnot
    """
    measurements = []
    for i in range(n):
        temp = read_temperature()
        measurements.append(temp)
        time.sleep(delay)
    return measurements

def compute_stats(values):
    """
    Spočítá min, max, průměr a směrodatnou odchylku
    """
    n = len(values)
    minimum = min(values)
    maximum = max(values)
    avg = sum(values) / n
    variance = sum((x - avg) ** 2 for x in values) / n
    stddev = math.sqrt(variance)
    return minimum, maximum, avg, stddev

# --- Hlavní smyčka ---
print("Stiskni tlačítko pro statistickou analýzu teploty...")
while True:
    wait_for_press()
    values = measure_statistics(5, 0.5)  # 5 měření s půlsekundovou pauzou
    minimum, maximum, avg, stddev = compute_stats(values)

    print("Naměřené hodnoty:", values)
    print(f"Min: {minimum:.1f} °C")
    print(f"Max: {maximum:.1f} °C")
    print(f"Průměr: {avg:.1f} °C")
    print(f"Směrodatná odchylka: {stddev:.2f} °C")
    print("-" * 30)
