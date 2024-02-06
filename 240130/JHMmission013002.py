import RPi.GPIO as GPIO
import time
red_pin = 4
green_pin = 5
blue_pin = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

try:
	while True:
		x = input("숫자를 입력하세요: ")
		if x=='1':
			GPIO.output(red_pin, True)
			GPIO.output(green_pin, True)
			GPIO.output(blue_pin, True)
			time.sleep(1)
		elif x=='2':
			GPIO.output(red_pin, False)
			GPIO.output(green_pin, False)
			GPIO.output(blue_pin, False)
			time.sleep(1)
		elif x=='3':
			for i in range(1,30):
				GPIO.output(red_pin, True)
				GPIO.output(green_pin, True)
				GPIO.output(blue_pin, True)
				time.sleep(i*0.001)
				GPIO.output(red_pin, False)
				GPIO.output(green_pin, False)
				GPIO.output(blue_pin, False)
				time.sleep((30-i)*0.001)
		elif x=='4':
			for i in range(1,30):
				GPIO.output(red_pin, True)
				GPIO.output(green_pin, True)
				GPIO.output(blue_pin, True)
				time.sleep((30-i)*0.001)
				GPIO.output(red_pin, False)
				GPIO.output(green_pin, False)
				GPIO.output(blue_pin, False)
				time.sleep(i*0.001)
		elif x=='5':
			for i in range(1,30):
				GPIO.output(red_pin, True)
				GPIO.output(green_pin, True)
				GPIO.output(blue_pin, True)
				time.sleep(i*0.001)
				GPIO.output(red_pin, False)
				GPIO.output(green_pin, False)
				GPIO.output(blue_pin, False)
				time.sleep((30-i)*0.001)
			for i in range(1,30):
				GPIO.output(red_pin, True)
				GPIO.output(green_pin, True)
				GPIO.output(blue_pin, True)
				time.sleep((30-i)*0.001)
				GPIO.output(red_pin, False)
				GPIO.output(green_pin, False)
				GPIO.output(blue_pin, False)
				time.sleep(i*0.001)	
		elif x=='6':
			sec = int(input("원하는 초 입력하세요(1초는 10입력) : "))
			for i in range(1,sec):
				GPIO.output(red_pin, True)
				GPIO.output(green_pin, True)
				GPIO.output(blue_pin, True)
				time.sleep(i*0.001)
				GPIO.output(red_pin, False)
				GPIO.output(green_pin, False)
				GPIO.output(blue_pin, False)
				time.sleep((sec-i)*0.001)
			for i in range(1,sec):
				GPIO.output(red_pin, True)
				GPIO.output(green_pin, True)
				GPIO.output(blue_pin, True)
				time.sleep((sec-i)*0.001)
				GPIO.output(red_pin, False)
				GPIO.output(green_pin, False)
				GPIO.output(blue_pin, False)
				time.sleep(i*0.001)
				
		elif x=='0':
			break

except KeyboardInterrupt:
	GPIO.cleanup()

