import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)     # LED 제어 핀 (외부로 출력하기 때문에 out)
GPIO.setup(27, GPIO.IN)      # PIR 센서 (외부에서 입력을 받기 때문에 in)
GPIO.setup(14, GPIO.OUT)     # GPIO buzz 핀(1)을 출력으로 설정
GPIO.setwarnings(False)

pwm = GPIO.PWM(14, 262)      # 초기 주파수를 262Hz로 설정

try:
    while True:
        pir_state = GPIO.input(27)
        if pir_state:
            GPIO.output(4, True)
            pwm.start(1)     # 1% duty cycle로 PWM 시작
            print("Motion Detected")
            time.sleep(0.5)
        else:
            GPIO.output(4, False)
            pwm.stop()        # PWM 중지
            time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()                # KeyboardInterrupt 발생 시 PWM 정지
    GPIO.cleanup()
