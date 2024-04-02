import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
led_red =4 
led_green=5
led_blue=6    

color_led = [led_red, led_green, led_blue]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in color_led:
    GPIO.setup(pin, GPIO.OUT)          # 각 LED핀을 출력으로 설정              
                            
GPIO.output(led_red,False)
GPIO.output(led_green,False)
GPIO.output(led_blue,False)

try:
    for i in range(10):
        for pin in color_led:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.5)
        for pin in color_led:
            GPIO.output(pin, GPIO.LOW)
        
except KeyboardInterrupt:
    pass
GPIO.cleanup()
    
