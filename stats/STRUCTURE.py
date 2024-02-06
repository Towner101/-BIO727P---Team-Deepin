import subprocess
import os

def run_structure(input_file, num_populations, output_prefix):
    """
    Run STRUCTURE software from Python.

    :param input_file: Path to the input file prepared for STRUCTURE.
    :param num_populations: Number of populations (K) to use in the analysis.
    :param output_prefix: Prefix for the output files generated by STRUCTURE.
    """
    # Construct the command to run STRUCTURE
    structure_cmd = f"structure -K {num_populations} -i {input_file} -o {output_prefix}"
    
    # Run the command
    subprocess.run(structure_cmd, shell=True, check=True)

# Example usage
input_file = "path/to/your_input_file"
num_populations = 3  # Example: Assuming you want to analyze for 3 populations
output_prefix = "structure_output"
run_structure(input_file, num_populations, output_prefix)


