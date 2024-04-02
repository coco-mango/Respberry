import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 설정
button_pin1 = 22
button_pin2 = 23
button_pin3 = 24
button_pin4 = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)     # LED 제어 핀 (외부로 출력하기 때문에 out)
GPIO.setup(14, GPIO.OUT)     # GPIO buzz 핀(1)을 출력으로 설정

# 버튼 핀의 입력설정
GPIO.setup(button_pin1, GPIO.IN)
GPIO.setup(button_pin2, GPIO.IN)
GPIO.setup(button_pin3, GPIO.IN)
GPIO.setup(button_pin4, GPIO.IN)

pwm = GPIO.PWM(14, 262)      # 초기 주파수를 262Hz로 설정


def song_play(song_name):
    scale = [523, 587, 659, 698, 784, 880, 988, 1047]
    song_len = len(song_name)
    pwm.start(1)
    for i in range(0, song_len):
        pwm.ChangeFrequency(scale[song_name[i] - 1])
        time.sleep(0.5)

try:
    while True:
        if GPIO.input(button_pin1) == GPIO.LOW:
            print("Song 1 : 똑같아요")
            song1 = [1, 1, 1, 1, 1, 3, 5, 5, 3, 1, 5, 5, 3, 5, 5, 3, 1, 1, 1,
                     5, 5, 3, 1, 5, 5, 5, 5, 5, 3, 1, 5, 5, 5,
                     5, 5, 3, 1, 5, 5, 5, 6, 5, 8, 5, 8, 5, 3, 2, 1]
            song_play(song1)
        if GPIO.input(button_pin2) == GPIO.LOW:
            print("Song 2 : 퐁당퐁당 ")
            song2 = [1, 2, 3, 3, 1, 3, 5, 6, 5,
                     1, 2, 3, 3, 1, 3, 5, 6, 5,
                     7, 5, 3, 7, 5, 3, 2, 2, 1, 2, 3, 5, 5,
                     6, 6, 5, 6, 8, 8, 8,
                     5, 5, 3, 2, 1,
                     2, 3, 1, 3, 5, 5, 5,
                     2, 3, 4, 3, 2, 1]
            song_play(song2)
        
        if GPIO.input(button_pin3) == GPIO.LOW:
            print("Song 3 : 빨강머리앤")
            song3 = [3, 4, 3, 1, 1, 2, 3, 4, 6, 8, 6, 7,
                     8, 8, 7, 6, 7, 6, 4, 3, 3, 4, 5, 6,
                     3, 4, 3, 3, 1, 2, 3, 4, 6, 8, 6, 7,
                     8, 8, 7, 6, 7, 6, 4, 3, 3, 4, 5, 6,
                     7, 7, 3, 6, 7, 8, 8, 8, 8, 7, 6, 7]
            song_play(song3)


except KeyboardInterrupt:
    pass

GPIO.cleanup()


