# File Processor

## Description
The File Processor is a Python script designed to read data from multiple .dat files located in a particular folder, process the data, and generate an output CSV file. The output CSV file contains the processed data along with a footer displaying the 2nd highest salary and the average salary.

## Dependencies
- Python 3.x
- pandas

## Process
1. The script reads data from all .dat files in the specified input folder.
2. It removes any duplicate entries from the combined dataset.
3. The script calculates the Gross Salary by summing up the basic salary and allowances for each record.
4. It identifies the 2nd highest salary and calculates the average salary.
5. The processed data is written to a CSV file in the specified output folder.
6. The script appends a footer to the output CSV file, displaying the 2nd highest salary and average salary.

## How to Run
1. Clone this repository to your local machine.
2. Install the required dependencies using pip
3. Place your .dat files containing the data to be processed in the `data/input_files/` directory.
4. Open a terminal or command prompt.
5. Navigate to the root directory of the cloned repository.
6. Run the script using the
7. Once the script finishes execution, you can find the processed data CSV file in the `data/output_files/` directory.


