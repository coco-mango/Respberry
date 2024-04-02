/* 3개의 Push button과 Buzzer를 테스트하는 회로를 구성하고 각 버튼에 따라 다른 동요를 플레이하는 프로그램           */
/* C에서는 wiringPi.h을 사용                                                                                     */
/* wiringPi.h에서는 buzzer를 1번 핀과 연결 (pwm0의 1이 라즈베리파이 GPIO18번)                                                */

#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>    
#include <time.h>

#define SW1 3
#define SW2 4
#define SW3 5
#define buzzer_pin 1

void song1(void);
void song2(void);
void song3(void);

int main(void){
    wiringPiSetup();                               // WiringPi 초기화

    pinMode(SW1,INPUT);
    pinMode(SW2,INPUT);
    pinMode(SW3,INPUT);
    pinMode(buzzer_pin, PWM_OUTPUT);                // 부저 핀을 PWM 출력으로 설정
    pwmSetClock(19);                                // PWM 클럭 설정 (19.2MHz 클럭)
    pwmSetMode(PWM_MODE_MS);
   
    pwmWrite(buzzer_pin, 0);                        // 처음에는 부저 소리 안나게

    while(1){
        if (digitalRead(SW1)==LOW){
        printf("Song Title : 똑같아요");
        song1();
        delay(500);}

    else if (digitalRead(SW2)==LOW){
        printf("Song Title : 퐁당퐁당");
        song2();
        delay(500);}

    else if (digitalRead(SW3)==LOW){
        printf("Song Title : 빨간머리앤");
        song3();
        delay(500);}
    }
    
    return 0;
}

void song1(void){
    const int scale[] = {523,587,659,698,784,880,988,1047};
    
    int song[] = {1, 1, 1, 1, 1, 3, 5, 5, 3, 1, 5, 5, 3, 5, 5, 3, 1, 1, 1,\
                     5, 5, 3, 1, 5, 5, 5, 5, 5, 3, 1, 5, 5, 5,\
                     5, 5, 3, 1, 5, 5, 5, 6, 5, 8, 5, 8, 5, 3, 2, 1};
    int song_size = sizeof(song)/sizeof(int);                

    for (int i = 0; i <song_size; i++) {                                    // 음계를 0.5초 간격으로 플레이
        //pwmSetRange(1000000 / scale[song[i]-1]);                       // PWM 주기 설정 (1초에 해당 음표의 주파수에 맞추기 위해)
        pwmWrite(buzzer_pin, 1000000 / scale[song[i]-1] / 100);        // PWM 출력 설정 (1% duty cycle로 설정하여 소리 출력)
        //pwmWrite(buzzer_pin, 500);
        delay(500);                                                         // 0.5초 간격으로 플레이
    }
    pwmWrite(buzzer_pin, 0);                                               //부저 종료
}



void song2(void){
    const int scale[] = {523,587,659,698,784,880,988,1047};
    
    int song[] = {1, 2, 3, 3, 1, 3, 5, 6, 5,\
                     1, 2, 3, 3, 1, 3, 5, 6, 5,\
                     7, 5, 3, 7, 5, 3, 2, 2, 1, 2, 3, 5, 5,\
                     6, 6, 5, 6, 8, 8, 8,\
                     5, 5, 3, 2, 1,\
                     2, 3, 1, 3, 5, 5, 5,\
                     2, 3, 4, 3, 2, 1};
    int song_size = sizeof(song)/sizeof(int);                

    for (int i = 0; i <song_size; i++) {                                    // 음계를 0.5초 간격으로 플레이
        //pwmSetRange(1000000 / scale[song[i]-1]);                       // PWM 주기 설정 (1초에 해당 음표의 주파수에 맞추기 위해)
        pwmWrite(buzzer_pin, 1000000 / scale[song[i]-1] / 100);        // PWM 출력 설정 (1% duty cycle로 설정하여 소리 출력)
        //pwmWrite(buzzer_pin, 500);
        delay(500);                                                         // 0.5초 간격으로 플레이
    }
    pwmWrite(buzzer_pin, 0);                                               //부저 종료
}

void song3(void){
    const int scale[] = {523,587,659,698,784,880,988,1047};
    
    int song[] = {3, 4, 3, 1, 1, 2, 3, 4, 6, 8, 6, 7,\
                     8, 8, 7, 6, 7, 6, 4, 3, 3, 4, 5, 6,\
                     3, 4, 3, 3, 1, 2, 3, 4, 6, 8, 6, 7,\
                     8, 8, 7, 6, 7, 6, 4, 3, 3, 4, 5, 6,\
                     7, 7, 3, 6, 7, 8, 8, 8, 8, 7, 6, 7};
    int song_size = sizeof(song)/sizeof(int);                

    for (int i = 0; i <song_size; i++) {                                    // 음계를 0.5초 간격으로 플레이
        //pwmSetRange(1000000 / scale[song[i]-1]);                       // PWM 주기 설정 (1초에 해당 음표의 주파수에 맞추기 위해)
        pwmWrite(buzzer_pin, 1000000 / scale[song[i]-1] / 100);        // PWM 출력 설정 (1% duty cycle로 설정하여 소리 출력)
        //pwmWrite(buzzer_pin, 500);
        delay(500);                                                         // 0.5초 간격으로 플레이
    }
    pwmWrite(buzzer_pin, 0);                                               //부저 종료
}
