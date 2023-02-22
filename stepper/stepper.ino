/*
  Rui Santos
  Complete project details at https://RandomNerdTutorials.com/esp32-stepper-motor-28byj-48-uln2003/
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files.
  
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  
  Based on Stepper Motor Control - one revolution by Tom Igoe
*/

#include <Stepper.h>
const int stepsPerRevolution = 2048;  // change this to fit the number of steps per revolution

// ULN2003 Motor Driver Pins A
#define IN1A 19
#define IN2A 18
#define IN3A 5
#define IN4A 17

// ULN2003 Motor Driver Pins B
#define IN1B 32
#define IN2B 33
#define IN3B 25
#define IN4B 26



// initialize the stepper library
Stepper myStepperB(stepsPerRevolution, IN1A, IN3A, IN2A, IN4A);
Stepper myStepper(stepsPerRevolution, IN1B, IN3B, IN2B, IN4B);

void setup() {
  // set the speed at 5 rpm
  myStepper.setSpeed(15);
  myStepperB.setSpeed(15);
  // initialize the serial port
  Serial.setRxBufferSize(16384);
  Serial.setTimeout(1);
  Serial.begin(250000);
}

int ds = 10;
float xp = 0;
float yp = 0;
int xpint = 0;
int ypint = 0;

bool manual = 0;


bool started = 0;
bool rdX = 0;
bool reading_num = 0;

String buff = "";
int xarr[16384/2] = { 0 };
int yarr[16384/2] = { 0 };
int xctr = 0, yctr = 0;
int arrctr = 0;



int digitsProcd = 0;
void loop() {
  while (Serial.available() > 0) {
    
    // for(int i = 0 ; i < 10; i++){
    //   Serial.println(">>>>>");
    // }
    // Serial.print(">>>>> >>>>> RENTER SERiAL AVAIL with arrctr");
    // Serial.println (arrctr);

    String cmd = Serial.readStringUntil(' ');
    int str_len = cmd.length() + 1;

    // Prepare the character array (the buffer)
    char char_array[str_len];

    // Copy it over
    cmd.toCharArray(char_array, str_len);


    if (isdigit(cmd[0])) {
      int val = atoi(char_array);
      // Serial.print("Read val raw: ");
      // Serial.println(val);

      if(arrctr%2==0)xarr[arrctr/2] = val;
      else yarr[arrctr/2] = val;
      arrctr++;
      digitsProcd++;
    }

    else if (cmd[0] == 'o'){
      yp = 0;
      xp = 0;
    }
  }

  if(arrctr  > 0){
    Serial.print("\n--- printing begins --- \n");

    // draw image fn
    for(int i = 0; i < arrctr/2 ; i++){

      // Serial.print("pt rd xarr ");
      // Serial.println(xarr[i]);
      // Serial.print("pt rd yarr ");
      // Serial.println(yarr[i]);
      // // at each point..
      int dx = xarr[i] - xp;
      int dy = yarr[i] - yp;


      // Serial.print("before xpos ");
      // Serial.println(xp);

      // Serial.print("before ypos ");
      // Serial.println(yp);

      // Serial.print("dx ");
      // Serial.println(dx);

      // Serial.print("dy ");
      // Serial.println(dy);

      // if(dx*dx+dy*dy==0) continue; //samespot
      // // if((abs(dx) + abs(dy)) < 64) delay(50);
      // if(abs(dx) > 1024 || abs(dy) > 1024) 
      // { // some times we get extra 0 or digit for no reason, small baud doesn't change it...
      //   Serial.println("ERROR!");
      //   delay(100);
      //   continue;
      // }

      // int xstep, ystep, xrem, yrem;
      // if(dx == 0){
      //   xstep = 0;
      //   ystep = dy;
      //   xrem = 0;
      //   yrem = 0;

      //   xp += xstep;
      //   yp += ystep;
      //   myStepper.step(xstep);
      //   myStepperB.step(ystep);
      // }
      // else if(dy == 0){
      //   xstep = dx;
      //   ystep = 0;
      //   xrem = 0;
      //   yrem = 0;
        
      //   xp += xstep;
      //   yp += ystep;
      //   myStepper.step(xstep);
      //   myStepperB.step(ystep);
      // }

      // else if(abs(dx) < abs(dy)){
      //   xstep = abs(dx)/dx;
      //   ystep = abs(dy/dx) * (dy/abs(dy)); //div by zero handled in case
      //   xrem = 0;
      //   yrem = dy % dx;
      //   while(xp != xarr[i]){
      //     yp+= ystep;
      //     xp+= xstep;
      //     myStepper.step(xstep);
      //     myStepperB.step(ystep);
      //   }
      //   yp += yrem;
      //   xp += xrem;
      //   myStepper.step(xrem);
      //   myStepperB.step(yrem);
      // }
      // else if (abs(dy) < abs(dx)){
      //   xstep = abs(dx/dy) * (dx/abs(dx));
      //   ystep = abs(dy)/dy;
      //   xrem = dx%dy;
      //   yrem = 0;
      //   while(yp != yarr[i]){
      //     yp += ystep;
      //     xp += xstep;
      //     myStepper.step(xstep);
      //     myStepperB.step(ystep);
      //   }
      //   yp += yrem;
      //   xp += xrem;
      //   myStepper.step(xrem);
      //   myStepperB.step(yrem);
      // }
      
      // else if (abs(dy) == abs(dx)){
      //   xstep = abs(dx)/dx;
      //   ystep = abs(dy)/dy;
      //   xrem = 0;
      //   yrem = 0;
      //   while(yp != yarr[i]){
      //     yp+= ystep;
      //     xp+= xstep;
      //     myStepper.step(xstep);
      //     myStepperB.step(ystep);
      //   }
      //   yp += yrem;
      //   xp += xrem;
      //   myStepper.step(xrem);
      //   myStepperB.step(yrem);
      // }


      // Serial.print("after xpos ");
      // Serial.println(xp);

      // Serial.print("after ypos ");
      // Serial.println(yp);
      // // xp = xarr[i];
      // // yp = yarr[i];
      // Serial.println("\n---\n");

      int steps;
      if (dx == 0) dx = 1;
      if (dy == 0) dy = 1;


      if(abs(dx) > abs(dy)){
        steps = abs(dx);
      }else{
        steps = abs(dy);
      }

      Serial.print("steps ");
      Serial.println(steps);
    
      float Xincrement = dx / (float) steps;
      float Yincrement = dy / (float) steps;

      Serial.print("xinc ");
      Serial.println(Xincrement);
      
      Serial.print("yinc ");
      Serial.println(Yincrement);



      Serial.print("xpf ");
      Serial.println(xp);
      
      Serial.print("ypf ");
      Serial.println(yp);


      for(int v=0; v < steps; v++)
      {
        xp += Xincrement;
        yp += Yincrement;

        if (xpint != round(xp)){
          int real_x_delta = round(xp) - xpint;
          myStepper.step(real_x_delta);
          xpint += real_x_delta;
        }

        if(ypint != round(yp)){
          int real_y_delta = round(yp) -ypint;
          myStepperB.step(-real_y_delta); // turn in opposite direction
          ypint += real_y_delta;
        }
      }
      
      Serial.print("xpint ");
      Serial.println(xpint);
      
      Serial.print("ypint ");
      Serial.println(ypint);
      Serial.print("\n---\n\n");
    }
    arrctr = 0;
    // zero the array
    // for (int i = 0; i < 16384/2; i++){
    //   xarr[i] = 0;
    //   yarr[i] = 0;
    // }
  }
    //endwhile
  // buff += c;
  // char c = Serial.read();
  // if(c == '#'){
  //   started=1;
  //   rdX = 1;
  // } // start
  // if(c == '!') started=0; //end
  // if(c == 'U') continue; //servo up
  // if(c == 'D') continue; //servo dwn

  // if(started){
  //   if(isdigit(c)&&!reading_num){
  //     char d = Serial.read()-'0';
  //     // draw from current to (c,d)

  //   }
  // }

  // char inch = Serial.read();
  // switch(inch){
  //   case 'w':  // up
  //     myStepperB.step(ds);
  //     yp+=ds;
  //     break;
  //   case 'a':
  //     myStepper.step(-ds);
  //     xp-=ds;
  //     break;
  //   case 's':
  //     myStepperB.step(-ds);
  //     yp-=ds;
  //     break;
  //   case 'd':
  //     myStepper.step(ds);
  //     xp+=ds;
  //     break;
  //   case 'o':
  //     xp = 0;
  //     yp=0;
  //     break;
  //   case 'm':
  //   manual = !manual;
  //   Serial.println(manual?"manual":"automatic (q)");
  //   break;
  //   case 'q':
  //   if(manual) break;
  //     myStepperB.step(-1024);
  //     myStepper.step(-1024);
  //     myStepperB.step(1024);
  //     myStepper.step(1024);
  //     break;
  // }

  // Serial.print("x: ");
  // Serial.print(xp);
  // Serial.print(" y: ");
  // Serial.print(yp);
  // Serial.println();

  // if(buff!="")Serial.print(buff);

  // if(buff.length()>0){

  //   int coordCtr = 0;
  //   const char s[2] = " ";
  //   char *token;

  //   int str_len = buff.length() + 1;

  // // Prepare the character array (the buffer)
  //   char char_array[str_len];

  // // Copy it over
  //   buff.toCharArray(char_array, str_len);

  //   /* get the first token */
  //   token = strtok(char_array, " ");

  //   /* walk through other tokens */
  //   while( token != NULL ) {
  //     Serial.print("token --> ");
  //     Serial.println(token);
  //     if(isdigit(token[0])){
  //       if(coordCtr%2==0){
  //         xarr[xctr] = atoi(token);
  //         Serial.print("add x ");
  //         Serial.println(xarr[xctr]);
  //         xctr++;
  //       }else{
  //         yarr[yctr] = atoi(token);
  //         Serial.print("add y ");
  //         Serial.println(yarr[yctr]);
  //         yctr++;
  //       }
  //       coordCtr++;
  //     }
  //     else{
  //       if(token[0] == 'U'){
  //         xarr[xctr++] = -1;
  //         yarr[yctr++] = -1;
  //         Serial.println("up");
  //       }
  //       if(token[0] == 'D'){
  //         xarr[xctr++] = -2;
  //         yarr[yctr++] = -2;
  //         Serial.println("down");
  //       }
  //     }
  //     token = strtok(NULL, s);
  //  }
  // }

  buff = "";
  // // step one revolution in one direction:
  // Serial.println("clockwise");
  // myStepper.step(stepsPerRevolution);
  // myStepperB.step(stepsPerRevolution);

  // delay(1000);

  // // step one revolution in the other direction:
  // Serial.println("counterclockwise");
  // myStepper.step(-stepsPerRevolution);
  // myStepperB.step(-stepsPerRevolution);
  // delay(1000);
}