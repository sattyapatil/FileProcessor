import os
import pandas as pd


def process_files(input_folder: str, output_folder: str):

    # Check if output folder exists, if not create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize an empty list to store DataFrames from all input files
    dfs = []

    # Iterate through all .dat files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.dat'):
            file_path = os.path.join(input_folder, filename)
            # Read data from current .dat file into a DataFrame
            df = pd.read_csv(file_path, sep='\t')  # Assuming tab-separated data
            # Append DataFrame from current file to dfs list
            dfs.append(df)

    # Concatenate all DataFrames in dfs list
    combined_data = pd.concat(dfs, ignore_index=True)

    # Remove duplicate rows
    combined_data.drop_duplicates(inplace=True)

    # Calculate Gross Salary
    combined_data['Gross Salary'] = combined_data['basic_salary'] + combined_data['allowances']

    # Calculate 2nd highest salary and average salary
    second_highest_salary = combined_data['Gross Salary'].nlargest(2).iloc[-1]
    average_salary = combined_data['Gross Salary'].mean()

    # Write combined data with Gross Salary to CSV file in the output folder
    output_file_path = os.path.join(output_folder, 'RESULT.csv')
    combined_data.to_csv(output_file_path, index=False)

    # Append footer with 2nd highest and average salary to the output CSV file
    with open(output_file_path, 'a') as f:
        f.write(f'\n\n2nd Highest Salary, {second_highest_salary}\n')
        f.write(f'Average Salary, {average_salary}\n')


if __name__ == "__main__":
    input_folder_path = 'data/input_files'
    output_folder_path = 'data/output_files'
    process_files(input_folder_path, output_folder_path)
