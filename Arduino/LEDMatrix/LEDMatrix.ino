#include <Wire.h>
#include <SenseMeAccelerometer.h>
#include <SenseMeLEDMatrix.h>
#include <LEDMatrixConstants.h>

static const uint8_t PROGMEM
 arrow[]=
 {
   B00011000,
   B00111100,
   B01111110,
   B00011000,
   B00011000,
   B00011000,
   B00011000,
   B00011000,
 };
static const uint8_t PROGMEM
 dot[]=
 {
   B00000000,
   B00000000,
   B00111100,
   B00111100,
   B00111100,
   B00111100,
   B00000000,
   B00000000,
 };
 
static const uint8_t PROGMEM
 hole[]=
 {
   B00000000,
   B00000000,
   B00111100,
   B00100100,
   B00100100,
   B00111100,
   B00000000,
   B00000000,
 };

void setup() {
  SenseMeLEDMatrix.begin();
  SenseMeLEDMatrix.clear();
  SenseMeAccelerometer.begin();
}

void loop() {
  
  float xyz[3];
  SenseMeAccelerometer.xyz(xyz);
  float x = xyz[0];
  float y = xyz[1];
  float z = xyz[2];
  if(x>1){
    SenseMeLEDMatrix.clear();
    SenseMeLEDMatrix.setRotation(2);
    SenseMeLEDMatrix.drawBitmap(0,0,arrow,8,8,LED_ON);   
  }
    if(x<-1){
    SenseMeLEDMatrix.clear();
    SenseMeLEDMatrix.setRotation(0);
    SenseMeLEDMatrix.drawBitmap(0,0,arrow,8,8,LED_ON);
  }
    if(y>0.98){
    SenseMeLEDMatrix.clear();
    SenseMeLEDMatrix.drawBitmap(0,0,hole,8,8,LED_ON);   
  }
    if(y<-0.98){
    SenseMeLEDMatrix.clear();
    SenseMeLEDMatrix.drawBitmap(0,0,dot,8,8,LED_ON);   
  }
    if(z>0.98){
    SenseMeLEDMatrix.clear();
    SenseMeLEDMatrix.setRotation(1);
    SenseMeLEDMatrix.drawBitmap(0,0,arrow,8,8,LED_ON);   
  }
    if(z<-0.98){
    SenseMeLEDMatrix.clear();
    SenseMeLEDMatrix.setRotation(3);
    SenseMeLEDMatrix.drawBitmap(0,0,arrow,8,8,LED_ON);   
  }
  SenseMeLEDMatrix.writeDisplay();
  delay(200);
  
    
}

