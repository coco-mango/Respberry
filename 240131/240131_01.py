import RPi.GPIO as GPIO
import time
import random
red_pin = 4
green_pin = 5
blue_pin = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)


def wrong_ans():
	print("오답입니다 !!")
	for i in range(1,3):
		GPIO.output(red_pin, True)
		time.sleep(1)
		GPIO.output(red_pin, False)
		time.sleep(1)

def correct_ans():
	print("정답입니다 !!")
	for i in [red_pin, green_pin, blue_pin]:
		GPIO.output(i, True)
		time.sleep(0.5)
		GPIO.output(i, False)
		time.sleep(0.5)


print("-"*60)
print("{0:^50}".format("빛의 삼원색 게임"))
print("{0:^40}".format("색을 확인하고 합쳐지면 어떤 색이 되는지 맞춰보자"))
print("-"*60)

try:
	while True:
		color = random.sample(["red","green","blue"],2)     #문자로 하면 아래에서 unsupported operand type(s) for &: 'str' and 'str' 에러 뜸
		print("*"*60)
		print("랜덤 컬러 : " ,color[0], color[1])

		print("-"*60)
		print("1. Yellow")
		print("2. Magenta")
		print("3. Cyan")
		print("-"*60)

		number = int(input("정답을 입력하세요 : "))
		if (((color[0]=="red" and color[1]=="green") or (color[1]=="red" and color[0]=="green")) and number ==1):
			correct_ans()
		elif (((color[0]=="red" and color[1]=="blue") or (color[1]=="red" and color[0]=="blue")) and number ==2):
			correct_ans()
		elif (((color[0]=="green" and color[1]=="blue") or (color[1]=="green" and color[0]=="blue")) and number ==3):
			correct_ans()
		else:
			wrong_ans()
		print("*"*60)
		print("\n")
		
except KeyboardInterrupt:
	GPIO.cleanup()

