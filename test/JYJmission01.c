#include <wiringPi.h>
#include <stdio.h>

#define led_red 7
#define led_green 21
#define led_blue 22

int main(void){
    if(wiringPiSetup() == -1)
		return 1;

    pinMode(led_red, OUTPUT);
    pinMode(led_green, OUTPUT);
    pinMode(led_blue, OUTPUT);
    
    for(int i=0;i<10;i++){
        digitalWrite(led_red,HIGH);
        digitalWrite(led_green,HIGH);
        digitalWrite(led_blue,HIGH);
        delay(1000);
        digitalWrite(led_red,LOW);
        digitalWrite(led_green,LOW);
        digitalWrite(led_blue,LOW);
        delay(1000);
    }
    
}
