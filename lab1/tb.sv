module fir_tb;

//Parameter Declaration
parameter data_bits = 10; //Bit-width of inputs
parameter coeff_bits = 10; //Bit-width of coefficients
parameter dataout_bits = data_bits + coeff_bits; //Bit-width of output
parameter N = 63;
integer i;
parameter N_input = 2000;
integer file;
integer count = 0;

//Input Signals Declaration
reg clk;
reg rst;
reg signed [data_bits-1:0] data_in;
wire signed [dataout_bits-1:0] data_out;

//400 Hz signal geeration
reg [31:0] counter_400hz; // Counter for 400 Hz signal
reg [31:0] counter_500hz; // Counter for 500 Hz signal
reg signed [data_bits-1:0] signal_400hz; // 400 Hz signal
reg signed [data_bits-1:0] signal_500hz; // 500 Hz signal

//Internal Signal declartion
reg signed [data_bits-1:0] mem[N_input-1:0];

//Wiring the unit test
FIR_TAP64 U1(	.clk(clk), 
		.rst(rst), 
		.data_in(data_in), 
		.data_out(data_out)
);
// Clock generation
always begin
        clk = 1; #250;
       	clk = 0; #250;	// 2kHz clock (500ns period -> 2kHz)
end

//Test procedure
initial begin 
	clk = 0;
	rst = 1;
	data_in = 0;
	$readmemb("in_bin.mem", mem, 0, N_input-1);
	
	#500;
	//Release Reset
	rst = 0;
	#500;
	//Input procedure
	for(i = 0 ; i < N_input-1 ; i = i+1) begin
		data_in = mem[i];
		$fwrite(file, "%b\n", data_out);
		#500;
	end
	// End simulation
	$finish;
end

initial begin
	$dumpfile("tb.vcd");
        $dumpvars;
	file = $fopen("sim.out", "w");
end

endmodule;


