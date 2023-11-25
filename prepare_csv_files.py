import glob
import os

RAW_DIR = "resources/raw"
DATA_DIR = "resources/data"

for csv_file in glob.glob(os.path.join(RAW_DIR, "*.csv")):

    filename = os.path.basename(csv_file)

    # Open the input file for reading and the output file for writing
    with open(csv_file, 'r') as input_file, open(os.path.join(DATA_DIR, filename), 'w', newline='') as output_file:
        # Iterate through each line in the input file
        for i, line in enumerate(input_file):
            # Check if the line meets a condition (customize this condition based on your needs)
            if i == 0 or ",Grid_ID," not in line:
                # If the condition is met, write the line to the output file
                output_file.write(line)