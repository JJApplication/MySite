---
title: 随机过程编程实验（C++）
tags:
  - c++
  - 技术
  - 随机过程
url: 642.html
id: 642
categories:
  - 网络技术
date: 2018-05-11 23:00:35
---

##### **随机模拟的基本方法又称为蒙特卡罗（Monte Carlo）方法。**

是Velleman与Von Neumann等人在20世纪40年代为研制核武器提出来的，已大量地运用于计算机仿真试验。随机模拟的典型步骤： 1、根据问题构建模拟系统 2、仿真系统中各种分布的随机变量 3、运行模拟系统，进行统计测量 4、分析数据，输出结果 主要工具 基本工具：C、C++等编程模拟、matlab 网络模拟：OPNET Modeler、NS2：大型网络仿真

### 伪随机数

*   **伪随机数的产生：**用户只需给定一个初始的 随机数（种子值），调用该算法，即可按某个固定的公式计算出下一个“随机”数。随后，以新产生出来的“随机”数作为种子，再计算出新的“随机”数。重复调用该算法即可产生出一系列的“随机”数，以满足系统仿真的需要。
*   伪随机数本质上不是随机的。但只要计算公式选择得当，通过比较严格地统计检验，仍然可以产生出一系列近似于U(0,1)分布并且相对独立的随机数流，这种随机数流对于大多数仿真模型，是能满足需要的。因此，仍然是目前广泛应用的工程方法。

**伪随机数产生方法** 线性同余法 1）设置y0，即设置种子 2）yn=kyn-1(mod N)，un=yn/N 三组常见的参数 N=1010，k=7，周期≈5×107 （IBM随机数发生器）N=231，k=216+3，周期≈5×108 （ran0） N=231-1，k=75，周期≈2×109 **泊松分布**   **正态分布**

### 实验平台

![CBZN0s.png](https://s1.ax1x.com/2018/05/11/CBZN0s.md.png)

### 实验平台介绍

> 实验平台包含的源文件 –StdAfx.cpp：VC工程自带文件，不能修改 –random.cpp和random.h：工程主文件，不能修改 –Scope.cpp和Scope.h ：画图程序，不能修改 –randomDlg.cpp和randomDlg.h：主界面程序，包括对各个按钮的动作的响应，还包括对各种随机变量的输入参数的设定 –MyRand.cpp和MyRand.h：各种分布的随机变量的产生程序，实验过程中主要完成MyRand.cpp中的函数即可

我们只需要修改myrand.cpp中的代码即可 **原始代码如下：**

```c++
// MyRand.cpp: implementation of the CMyRand class.
//
//////////////////////////////////////////////////////////////////////

#include "stdafx.h"
#include "random.h"
#include "MyRand.h"
#include "math.h"

#ifdef _DEBUG
#undef THIS_FILE
static char THIS_FILE[]=__FILE__;
#define new DEBUG_NEW
#endif

//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////

CMyRand::CMyRand()
{

}

CMyRand::~CMyRand()
{

}

void CMyRand::MyRandInit(void)
{
	N = 0x7FFFFFFF; //2^31-1
	K = 16807;      //7^5
	seed = 2;
}

/*函数功能，采用线性同余法，根据输入的种子数产生一个伪随机数，如果种子不变，
  则将可以重复调用产生一个伪随机序列

  利用CMyRand类中定义的全局变量：S, K, N, Y。
  其中K和N为算法参数，S用于保存种子数，Y为产生的随机数
*/
unsigned int CMyRand::MyRand(unsigned int seed)
{
	//添加伪随机数产生代码
```


​    
```c++
	return Y;
}

/*函数功能，产生一个在min~max范围内精度为4位小数的平均分布的随机数
*/
double CMyRand::AverageRandom(double min,double max)
{
	double dResult;

	dResult = 0;

	//添加均匀分布随机变量产生代码
```


​    
```c
	return dResult;
}

/*函数功能，在min 到max 范围内产生正态分布的随机数
miu,最大概率密度处的随机变量，即产生的随机数中,概率最大的那个
sigma
*/
double CMyRand::NormalRandom(double miu, double sigma, double min, double max)
{
	double dResult;

	dResult = 0;

	//添加正态分布随机变量产生代码
```


​    
```c++
	return dResult;
}

/*函数功能，产生指数分布的随机数
*/
double CMyRand::ExpRandom(double lambda, double min, double max)
{
	double dResult = 0.0;

	//添加指数分布随机变量产生代码
```


​    
```c++
	return dResult;
}

/*函数功能，产生泊松分布的随机数
*/
unsigned int CMyRand::PoisonRandom(double lambda, double min, double max)
{
	unsigned int dResult = 0;

	//添加泊松分布随机变量产生代码

	return dResult;
}
```


​    
```c++
/*函数功能，计算任意分布的随机过程的均值
*/
double CMyRand::Ex(void)
{
	double Ex = 0;

	//添加均值计算代码
```


​    
```c
	return Ex;
}

/*函数功能，计算随机过程的自相关序列
*/
double* CMyRand::Rx(double lambda, int points)
{
	int m,I;
	double *Rx = (double*)malloc((2*points+1)*sizeof(double));

	//添加自相关序列产生代码
	//产生的自相关序列存入Rx中，Rx可当作数组使用
	//不要在本函数中释放该数组!
```


​    	
```c++
	return Rx;
}
```

**修改后的代码**

```c++
// MyRand.cpp: implementation of the CMyRand class.
//
//////////////////////////////////////////////////////////////////////

#include "stdafx.h"
#include "random.h"
#include "MyRand.h"
#include "math.h"

#ifdef _DEBUG
#undef THIS_FILE
static char THIS_FILE[]=__FILE__;
#define new DEBUG_NEW
#endif

//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////

CMyRand::CMyRand()
{

}

CMyRand::~CMyRand()
{

}

void CMyRand::MyRandInit(void)
{
	N = 0x7FFFFFFF; //2^31-1
	K = 16807;      //7^5
	seed = 2;
}

/*函数功能，采用线性同余法，根据输入的种子数产生一个伪随机数，如果种子不变，
  则将可以重复调用产生一个伪随机序列

  利用CMyRand类中定义的全局变量：S, K, N, Y。
  其中K和N为算法参数，S用于保存种子数，Y为产生的随机数
*/

unsigned int CMyRand::MyRand(unsigned int seed)
{   if(S==seed)
      Y=K*Y%N;
     else
	 { 
		 S=seed;
		 Y=K*seed%N;
	 }

	//添加伪随机数产生代码
```


​    
```c++
	return Y;
}

/*函数功能，产生一个在min~max范围内精度为4位小数的平均分布的随机数
*/
double CMyRand::AverageRandom(double min,double max)
{
	double dResult;

	dResult = 0;
	dResult=(double)MyRand(seed)/N;
	dResult=dResult*(max-min)+min;
```


​    
​    	//添加均匀分布随机变量产生代码


​    
```c++
	return dResult;
}

/*函数功能，在min 到max 范围内产生正态分布的随机数
miu,最大概率密度处的随机变量，即产生的随机数中,概率最大的那个
sigma
*/
double CMyRand::NormalRandom(double miu, double sigma, double min, double max)
{
	double dResult;

	dResult = 0;
	for(int i=0;i<12;i++)
		 dResult+=AverageRandom(min,max);
	     dResult=(dResult-6)/(max-min);
		 dResult=dResult*sigma+miu;
```


​    
​    
​    	//添加正态分布随机变量产生代码


​    
```c++
	return dResult;
}

/*函数功能，产生指数分布的随机数
*/
double CMyRand::ExpRandom(double lambda, double min, double max)
{
	double dResult = 0.0;
	while(dResult<0.01)
	{  dResult=AverageRandom(min,max);

	}
	dResult=-1.0*log(dResult)/lambda;
```


​    
​    	//添加指数分布随机变量产生代码


​    
```c++
	return dResult;
}

/*函数功能，产生泊松分布的随机数
*/
unsigned int CMyRand::PoisonRandom(double lambda, double min, double max)
{
	unsigned int dResult = 0;
	double u=AverageRandom(min,max);
	int i=0;
	double p=exp(-1*lambda);
	double F=p;
	while(u>=F)
	{ p=lambda*p/(i+1);
	  F+=p;
	  i++;
	}
	dResult=i;
```


​    
```c++
	//添加泊松分布随机变量产生代码

	return dResult;
}
```


​    
```c++
/*函数功能，计算任意分布的随机过程的均值
*/
double CMyRand::Ex(void)
{
	double Ex = 0;
	int m;
	double sum=0;
	for (m=0;m<1000;m++)
	{ sum+=NormalRandom(0,1.4,0,1);
	 
	}
     Ex=sum/m;
```


​    
​    
​    	//添加均值计算代码


​    
```c++
	return Ex;
}
```


​    
```c++
/*函数功能，计算随机过程的自相关序列
*/
double* CMyRand::Rx(double lambda, int points)
{
	int m,I=5;
	double *Rx = (double*)malloc((2*points+1)*sizeof(double));

	//添加自相关序列产生代码
	//产生的自相关序列存入Rx中，Rx可当作数组使用
	//不要在本函数中释放该数组!
   for(m=-points;m<points;m++)
   {  Rx[(m+points)]=I*I*exp(-2*lambda*abs(m));
   }
```


​    	
```c++
	return Rx;
```

![](http://file.mgek.cc/images/blog/random-process-homework-1.webp)

 提供源代码和流程图 **最终的代码随机模拟结果如图（上为随机数，下为分布曲线）** 
![](http://file.mgek.cc/images/blog/random-process-homework-2.webp)
![](http://file.mgek.cc/images/blog/random-process-homework-3.webp)
![](http://file.mgek.cc/images/blog/random-process-homework-4.webp)
![](http://file.mgek.cc/images/blog/random-process-homework-5.webp)
![](http://file.mgek.cc/images/blog/random-process-homework-6.webp)
![](http://file.mgek.cc/images/blog/random-process-homework-7.webp)
![](http://file.mgek.cc/images/blog/random-process-homework-8.webp)
![](http://file.mgek.cc/images/blog/random-process-homework-9.webp)
![](http://file.mgek.cc/images/blog/random-process-homework-10.webp)
![](http://file.mgek.cc/images/blog/random-process-homework-11.webp)