/* Buzzer를 테스트하는 회로를 구성하고 동요를 플레이하는 프로그램                                                   */
/* C에서는 wiringPi.h을 사용                                                                                     */
/* wiringPi.h에서는 buzzer를 1로 설정하고 라즈베리파이 GPIO18번에 연결                                             */

#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>    
#include <time.h>

#define buzzer_pin 1                                                       // 부저 핀을 GPIO 핀 번호 1로 정의               

int main(void){
    if(wiringPiSetup() == -1)                                              // WiringPi 초기화하고 실패하면 1 반환
		return 1;                                                           
  
    pinMode(buzzer_pin, PWM_OUTPUT);                                       // 부저 핀을 PWM 출력으로 설정
    pwmSetClock(19);                                                       // PWM 클럭 설정 (19.2MHz 클럭)
    pwmSetMode(PWM_MODE_MS);                                               // PWM 모드를 MS 모드로 설정
   
    pwmWrite(buzzer_pin, 0);                                               // 처음에는 부저 소리 안나게

    printf("Song Title : 똑같아요\n");                                     // 동요 제목 출

    const int scale[] = {523,587,659,698,784,880,988,1047};               // 음계에 해당하는 주파수를 배열로 정의
    // 연주할 노래를 숫자로 표현한 배열
    int song[] = {1, 1, 1, 1, 1, 3, 5, 5, 3, 1, 5, 5, 3, 5, 5, 3, 1, 1, 1,\       
                     5, 5, 3, 1, 5, 5, 5, 5, 5, 3, 1, 5, 5, 5,\
                     5, 5, 3, 1, 5, 5, 5, 6, 5, 8, 5, 8, 5, 3, 2, 1};
    int song_size = sizeof(song)/sizeof(int);                             // 동요 길이 계산           

    for (int i = 0; i <song_size; i++) {                                  // 음계를 0.5초 간격으로 플레이
        pwmSetRange(1000000 / scale[song[i]-1]);                          // PWM 주기 설정 (1초에 해당 음표의 주파수에 맞추기 위해)
        pwmWrite(buzzer_pin, 1000000 / scale[song[i]-1] / 10);            // PWM 출력 설정 (1% duty cycle로 설정하여 소리 출력)
        delay(500);                                                       // 0.5초 간격으로 플레이
    }
    pwmWrite(buzzer_pin, 0);                                              //부저 종료
    
    return 0;                                                             // 프로그램 종료
}
