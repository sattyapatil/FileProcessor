**File Processor Design Specification**

**Project Name:** File Processor

**Description:**
The File Processor is a Python application designed to process data from multiple .dat files located in a particular folder and generate an output CSV file. The output file includes processed data along with a footer containing the 2nd highest salary and average salary.

**Used Libraries:**
- pandas

**Process:**
1. **Input Data Handling:**
   - Read data from multiple .dat files located in a specified input folder.
   - Parse the data and load it into pandas DataFrames.
   
2. **Data Processing:**
   - Combine data from all input files into a single DataFrame.
   - Remove any duplicate entries to ensure data integrity.
   - Calculate the Gross Salary by summing up the basic salary and allowances for each record.
   - Identify the 2nd highest salary and calculate the average salary.

3. **Output Generation:**
   - Write the processed data along with the calculated Gross Salary to a CSV file in the specified output folder.
   - Append a footer to the output CSV file, displaying the 2nd highest salary and average salary.

**Pros:**
- Efficient processing of large volumes of data.
- Utilizes pandas library for easy data manipulation and analysis.
- Provides flexibility in handling different file formats and data structures.
- Simplifies data cleaning and transformation tasks.

**Cons:**
- Loading all data into memory may lead to memory issues with extremely large datasets.
- Limited scalability for processing very large datasets due to memory constraints.
