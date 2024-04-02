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

#생성한 패턴 저장 변수

#LED 배열을 랜덤하게 생성하는 함수 생성
def rand_pattern():
	return random.choices([red_pin,green_pin,blue_pin], k=6)
#패턴과 시간을 입력받고 해당 패턴을 시간만큼 점등하는 함수 생성
pattern = rand_pattern()
def led_pattern(pattern,waittime):    #waittime이 아니라 time으로 쓰면 AttributeError: 'int' object has no attribute 'sleep' 에러 생김
	for i in pattern:
		GPIO.output(i, True)
		time.sleep(waittime)
		GPIO.output(i, False)
		time.sleep(waittime)

#오답이었을 때의 점등 패턴 함수 생성
def wrong_ans():
	print("오답입니다 !!")
	print("정답은", pattern, "입니다.")
	for i in range(1,3):
		GPIO.output(red_pin, True)
		time.sleep(1)
		GPIO.output(red_pin, False)
		time.sleep(1)

#정답이었을 때의 점등 패턴 함수 생성
def correct_ans():
	print("정답입니다 !!")
	for i in [red_pin, green_pin, blue_pin]:
		GPIO.output(i, True)
		time.sleep(0.5)
		GPIO.output(i, False)
		time.sleep(0.5)


print("안녕하세요 LED 패턴 암기 테스트입니다")
time.sleep(0.5)
print("패턴이 랜덤하게 생성되어 LED가 점등됩니다")
time.sleep(0.5)
print("6개의 패턴을 기억하신 후 점등이 끝나면 정답을 입력하세요")
time.sleep(0.5)
print("엔터키를 누르면 시작합니다")
input()
#1.패턴 생성
print("패턴 생성중 ...")
rand_pattern()
#2.led 점등
led_pattern(pattern, 1)
#3.정답 입력
print("정답을 입력하세요 (엔터키로 구분)")
print("red : 4, green : 5, blue :6")
answer = []
for i in range(6):
	answer.append(int(input()))
#4.정답확인
if pattern == answer:
	correct_ans()
else:
	wrong_ans()
