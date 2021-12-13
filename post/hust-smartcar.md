---
title: 华中科技大学——智能小车设计实验
tags:
  - 学习笔记
  - 技术
  - 电工实习
url: 743.html
id: 743
categories:
  - Tips
date: 2018-06-18 22:14:26
---

利用所给的具有蓝牙模块的智能小车设计，具备自动循迹，红外感应，蓝牙操作的智能小车。 利用灰度传感器实现自动寻迹 利用红外传感器实现红外遥感启动 使用蓝牙串口助手连接小车实现蓝牙操控 实现代码如下

```c
int  L_state=0;          

void setup()
{
  Serial.begin(9600);
  pinMode( 18, INPUT);
  pinMode( 14, INPUT);
  pinMode( 17, INPUT);
  pinMode( 16, INPUT);
  pinMode( 10, OUTPUT);
  pinMode( 6, OUTPUT);
  pinMode( 5, OUTPUT);
  pinMode( 9, OUTPUT);
  analogWrite(5 , 0);

  analogWrite(6 , 0);

  analogWrite(9 , 0);

  analogWrite(10 , 0);

}

void loop()
{
  char gets =   Serial.read();
  if (gets=='l')
  {
    analogWrite(5 , 0);
    analogWrite(6 , 100);
    analogWrite(9 , 0);
    analogWrite(10 , 0);
    L_state=0;
  }
  else if (gets=='r')
  {
    
      analogWrite(5 , 0);
      analogWrite(6 , 0);
      analogWrite(9 , 0);
      analogWrite(10 , 100);
      L_state=0;
   }
  else if  (gets=='f')
  {
      analogWrite(5 , 0);
      analogWrite(6 , 180);
      analogWrite(9 , 0);
      analogWrite(10 , 130);
      L_state=0;
   }
   else if( gets=='s')
  {
     
      analogWrite(5 , 0);
      analogWrite(6 , 0);
      analogWrite(9 , 0);
      analogWrite(10 , 0);
      L_state=0;
   }
   else if( gets=='b')
  {
         
      analogWrite(5 , 180);
      analogWrite(6 , 0);
      analogWrite(9 , 130);
      analogWrite(10 , 0);
      L_state=0;
   }
   else if( gets=='k')   
      L_state=1;         //设置红外追踪状态标志       
   else if( gets=='e')
      L_state=2; 

   //红外追踪
   if(L_state==1)     track();

  //自动寻迹
   else if(L_state==2)    trace();

}
```


​    
```c
void track()
{
  if (( !( digitalRead(14) ) && digitalRead(18) ))
  {
    analogWrite(5 , 0);
    analogWrite(6 , 255);
    analogWrite(9 , 0);
    analogWrite(10 , 0);
  }
  else
  {
    if (( !( digitalRead(18) ) && digitalRead(14) ))
    {
      analogWrite(5 , 0);
      analogWrite(6 , 0);
      analogWrite(9 , 0);
      analogWrite(10 , 230);
    }
    else
    {
      if (( !( digitalRead(14) ) && !( digitalRead(18) ) ))
      {
        analogWrite(5 , 0);
        analogWrite(6 , 255);
        analogWrite(9 , 0);
        analogWrite(10 , 230);
      }
      else
      {
        analogWrite(5 , 0);
        analogWrite(6 , 0);
        analogWrite(9 , 0);
        analogWrite(10 , 0);
      }
    }
  }
}
```


​    
​    
```c
void trace()
{
  if (( !( digitalRead(16) ) && digitalRead(17) ))
  {
    analogWrite(5 , 0);
    analogWrite(6 , 220);
    analogWrite(9 , 0);
    analogWrite(10 , 0);
  }
  else
  {
    if (( !( digitalRead(17) ) && digitalRead(16) ))
    {
      analogWrite(5 , 0);
      analogWrite(6 , 0);
      analogWrite(9 , 0);
      analogWrite(10 , 220);
    }
    else
    {
      if (( digitalRead(16) && digitalRead(17) ))
      {
        analogWrite(5 , 0);
        analogWrite(6 , 180);
        analogWrite(9 , 0);
        analogWrite(10 , 150);
      }
      else
      {
        analogWrite(5 , 0);
        analogWrite(6 , 0);
        analogWrite(9 , 0);
        analogWrite(10 , 0);
      }
    }
  }
}
```

因为使用的小车存在磨损，在试验的过程中小车的两个轮子的转速可能不同需要使用代码修改两车轮的转速。

灰度传感器的摆放影响了小车在弯道转弯时候的灵敏度，如果设置的速度过快会使小车冲出跑道

 ![](http://file.mgek.cc/images/blog/hust-smartcar.webp)