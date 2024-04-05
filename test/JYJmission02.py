# Buzzer를 테스트하는 회로를 구성하고 동요를 플레이하는 프로그램
# Python에서는 GPIO 사용                                              
# 라즈베리파이에 pin을 꽂을 때는 buzzer는 14번에 연결

import RPi.GPIO as GPIO                                 # RPi.GPIO 라이브러리를 가져오리
import time                                             # 시간 관련 기능을 사용하기 위해 time 모듈 가져오기

GPIO.setwarnings(False)                                 # GPIO 핀 설정 시 발생하는 경고를 무시
GPIO.setmode(GPIO.BCM)                                  # GPIO 핀 번호를 BCM 모드로 설정

buzzer = 14                                             # 부저 핀을 GPIO 핀 번호 14로 설정
GPIO.setup(buzzer, GPIO.OUT)                            # 부저 핀을 출력으로 설정

pwm = GPIO.PWM(14, 1.0)                                 # PWM 객체를 생성하고, 초기 주파수를 1Hz로 설정
pwm.start(1.0)                                          # PWM 신호를 출력하기 시작(듀티 사이클 1%)

scale = [523, 587, 659, 698, 784, 880, 988, 1047]       # 음계에 해당하는 주파수를 리스트로 정의
# 연주할 노래를 숫자로 표현한 리스트
song = [1, 1, 1, 1, 1, 3, 5, 5, 3, 1, 5, 5, 3, 5, 5, 3, 1, 1, 1,
                5, 5, 3, 1, 5, 5, 5, 5, 5, 3, 1, 5, 5, 5,
                5, 5, 3, 1, 5, 5, 5, 6, 5, 8, 5, 8, 5, 3, 2, 1]  
song_len = len(song)                                    # 동요 길이를 계산
print("Song Title : 똑같아요")                           # 동요 제목을 출력
for i in range(0, song_len):                            # 동요의 길이만큼 반복
    pwm.ChangeFrequency(scale[song[i] - 1])             # PWM의 주파수를 변경하여 음계에 해당하는 소리를 출력
    time.sleep(0.5)                                     # 0.5초 기다림
pwm.stop()                                              # PWM 신호를 정지
GPIO.cleanup()                                          # GPIO 설정을 초기화
