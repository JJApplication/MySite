---
title: verilog实现50mhz分频
tags:
  - verilog
  - 技术
url: 502.html
id: 502
categories:
  - 网络技术
date: 2018-03-27 15:47:07
---

```verilog
`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:39:27 12/11/2017 
// Design Name: 
// Module Name:    time50 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module time50(clk_50MHZ,clk_1HZ);
input clk_50MHZ;
reg [25:0]Count_DIV=0;
output reg clk_1HZ=0;

parameter CLK_Freq=50000000;//定义时钟信号为50mhz
always@(posedge clk_50MHZ)  begin
	    if(Count_DIV<(CLK_Freq/2-1))
		   Count_DIV<=Count_DIV+1'b1;
		 else  begin
		   Count_DIV<=0;
			clk_1HZ=~clk_1HZ;
	    end
	 end
	endmodule//对50mhz进行分频，达到一半频率进行一次分频
```


​    

**在进行分频时，clk_freq所除数代表分频数，例如分频为1hz，即为freq\*1/2，分频为2hz即为freq\*2/2**