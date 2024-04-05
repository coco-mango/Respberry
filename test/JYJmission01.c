/* Red, Green, Blue LED를 테스트하는 회로를 구성하고 10번 깜박이는 프로그램  */
/* C언어에서는 wiringPi 사용                                              */
/* 라즈베리파이에 pin을 꽂을 때는 red, green, blue 순서대로 4,5,6에 연결    */

#include <wiringPi.h>                    // 라즈베리파이의 GPIO(General Purpose Input Output)핀에 엑세스 하기 위한 C/C++ 라이브러리
#include <stdio.h>

#define led_red 7                        // RED LED의 GPIO 핀 번호 정의
#define led_green 21                     // GREEN LED의 GPIO 핀 번호 정의
#define led_blue 22                      // BLUE LED의 GPIO 핀 번호 정의

int main(void){
    if(wiringPiSetup() == -1)           //Wiringpi 라이브러리 초기화에 실패하면(-1) 1을 반환
		return 1;

    pinMode(led_red, OUTPUT);           // RED LED 핀을 출력모드로 설정
    pinMode(led_green, OUTPUT);         // GREEN LED 핀을 출력모드로 설정
    pinMode(led_blue, OUTPUT);          // BLUE LED 핀을 출력모드로 설정
    
    for(int i=0;i<10;i++){              // LED ON-OFF 10번 반복
        digitalWrite(led_red,HIGH);     // RED LED ON
        digitalWrite(led_green,HIGH);   // GREEN LED ON
        digitalWrite(led_blue,HIGH);    // BLUE LED ON
        delay(1000);                    // 1000밀리초(=1초) 기다림
        digitalWrite(led_red,LOW);      // RED LED OFF
        digitalWrite(led_green,LOW);    // GREEN LED OFF
        digitalWrite(led_blue,LOW);     // BLUE LED OFF
        delay(1000);
    }
    
}
