#Makefile commands
make ini: 
	- to create the input signals and change it into 10-bit fixed point representation - S1.8
	- to change the coefficients into 10-bit fixed point representation - S1.8

make run:
	- Compile and create a .vcd file for gtkwave to compile

make graph:
	- Graph the output signals along with 400Hz signal and 500Hz signal

make clean:
	- Cleaning up

