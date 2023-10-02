# Declaring variables
FIR_SRC = FIR_TAP64.sv
TB_SRC = tb.sv
IVERILOG = /ee/166/iverilog/bin/iverilog
VVP = /ee/166/iverilog/bin/vvp
OUTPUT_FILE = sim
LOG_FILE = output.log
 
# Preprocess step
ini: 
	python pre_process.py

# Rule to compile and run the simulation
run: $(FIR_SRC) $(TB_SRC)
	$(IVERILOG) -o $(OUTPUT_FILE) -g2005-sv $(FIR_SRC) $(TB_SRC)
	$(VVP) $(OUTPUT_FILE) | tee $(LOG_FILE)

# Post-process step
graph: 
	python post_process.py

# Clean up generated files
clean:
	rm -rf $(LOG_FILE) $(OUTPUT_FILE)

