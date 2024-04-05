# Red, Green, Blue LED를 테스트하는 회로를 구성하고 10번 깜박이는 프로그램 
# Python에서는 GPIO 사용                                              
# 라즈베리파이에 pin을 꽂을 때는 red, green, blue 순서대로 4,5,6에 연결 

import RPi.GPIO as GPIO                    # RPi.GPIO는 RaspberryPi의 GPIO 핀을 제어하기 위한 파이썬 라이브러리
import time

# GPIO 핀 번호 설정
led_red =4                                 # RED LED의 GPIO 핀 번호 정의
led_green=5                                # GREEN LED의 GPIO 핀 번호 정의
led_blue=6                                 # BLUE LED의 GPIO 핀 번호 정의

color_led = [led_red, led_green, led_blue] # LED의 GPIO 핀 번호를 리스트에 정의

GPIO.setwarnings(False)                    # 경고 발생하면 무시
GPIO.setmode(GPIO.BCM)                     # GPIO 핀 번호를 BCM 모드로 설정

for pin in color_led:
    GPIO.setup(pin, GPIO.OUT)              # 각 LED핀을 출력모드로 설정              
                            
GPIO.output(led_red,False)                 # 일단 모든 LED OFF
GPIO.output(led_green,False)
GPIO.output(led_blue,False)

try:
    for i in range(10):                    # 10번 ON-OFF 반복
        for pin in color_led:
            GPIO.output(pin, GPIO.HIGH)    # LED ON
            time.sleep(0.5)                # 0.5초 기다림
        for pin in color_led:              
            GPIO.output(pin, GPIO.LOW)     # LED OFF
        
except KeyboardInterrupt:
    pass
GPIO.cleanup()                             # GPIO 설정 초기화
    
