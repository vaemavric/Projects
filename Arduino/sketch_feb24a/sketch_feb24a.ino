#include <Wire.h>
#include <SenseMeBluetooth.h>
#include <SenseMe.h>
#include <SenseMeLEDMatrix.h>
#include <LEDMatrixConstants.h>
//Author: VS
//An AT Command terminal for Bluetooth. 

//Allow debug print statement in the drivers
#define DEBUG
#define BTDELAY 100


void BTsetCmdMode(int);
void setup() 
{
  Serial.begin(9600);
  SenseMeBluetooth.begin();
  SenseMeLEDMatrix.begin();
  SenseMeLEDMatrix.clear();
  
  
  delay(3000); 
  // Uncomment the line to carry out once
  //SenseMeBluetooth.setMaster();
  
  //Start AT Command Mode
  BTSERIAL.begin(9600);
  SenseMeBluetooth.setCmdMode(0);
}


int mode = 0;

char c;
String s = "";
int x = 0;
void loop() 
{
  
  if(Serial1.available())
  {
    c = Serial1.read();
    s= s+String(c);
  }else{
    
    SenseMeLEDMatrix.scrollText(s);
    if(x<3){
      s="";
      x=0;
    }
    x= x+1;
    delay(100);
  }
  //s="";
}


}


