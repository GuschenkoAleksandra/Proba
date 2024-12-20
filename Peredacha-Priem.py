from machine import UART
import time

uart1 = UART(1, baudrate = 115200, tx=33, rx=34)

while True:
    uart1.write('Hello, ESP32!')
    time.sleep(1)
    print(uart1.read())
    time.sleep(1)

#ampy --port COM7 run C:\Users\Mikhail\Downloads\Peredacha-Priem.py