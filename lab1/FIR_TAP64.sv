`timescale 1ns / 1ps

module FIR_TAP64(clk, rst, data_in, data_out);
//Parameter Declaration
parameter data_bits = 10; //Bit-width of inputs
parameter coeff_bits = 10; //Bit-width of coefficients
parameter dataout_bits = data_bits + coeff_bits; //Bit-width of output
parameter N = 63;
integer i;

//Input Signals Declaration
input clk;
input rst;
input logic [data_bits-1:0] data_in;
output logic [dataout_bits-1:0] data_out;

//Internal signal declaration
reg signed [coeff_bits-1:0] coeff[N-1:0];	//Coefficient register
reg signed [data_bits-1:0] shift_reg[N-1:0];	//Shift Register
reg signed [dataout_bits-1:0] product[N-1:0];	//Product Register
reg signed [dataout_bits-1:0] sum;		//Summation out
reg signed [data_bits-1:0] datain_buf;		//Input Buffer

assign data_out = sum;

//Load the coefficients into the signal
initial begin
	//Read the coeff from the .mem file
	$readmemb("coeff_bin.mem", coeff, 0, N-1);
    	//Testing
	// Display all coefficients
    	//$display("Printing all coefficients:");
    	//for(int i = 0; i < N; i = i + 1) begin
        	//$display("coeff[%0d] = %b", i, coeff[i]);
    	//end
	
end

//Logic for the input buffer
always_ff @(posedge clk)
begin
	if(rst) begin
		for (i = 0; i < N; i = i + 1) begin
                	shift_reg[i] = 0;
                	product[i] = 0;
		end
		sum <= 0;
		datain_buf <= 0;	
	end
	else begin
		//Inputing the data and shifting the register
		datain_buf <= data_in;
		for (i = N - 1; i > 0; i = i - 1) begin
			shift_reg[i] <= shift_reg[i - 1];
		end
		shift_reg[0] <= datain_buf;
		
		//Multiplying
		for(i = 0; i < N; i = i + 1) begin
			product[i] = shift_reg[i] * coeff[i];
		end

		//Compute sum
		sum = 0;
		for(int i = 0; i < N; i = i + 1) begin
			sum = sum + product[i];
		end
			
	end
end

endmodule;
