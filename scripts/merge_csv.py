import csv
from os import walk

headers = ['date','lat','lon']
cruise_data=[]

file_names = list()

for root, dirc, files in walk('C:\\Users\\bonny\\Downloads\\EN259_EN587'):
    for FileName in files:
        file_names.append(FileName)

for file in file_names:

    input_csv_path = "C:\\Users\\bonny\\Downloads\\EN259_EN587\\%s" % file
    output_csv_path = "C:\\Users\\bonny\\Downloads\\EN259_EN587\\EN259_EN587_points"



    with open(input_csv_path, 'r') as input_file:
        # Read the existing data
        reader = csv.reader(input_file)
        for row in reader:
            cruise_name=file[0:5]
            modified_row=[cruise_name]+row
            print(modified_row)
            cruise_data.append(modified_row)

    # Open the output CSV file for writing
    with open(output_csv_path, 'w', newline='') as output_file:
        # Write the headers
        writer = csv.writer(output_file)
        writer.writerow(headers)
        # Write the existing data
        writer.writerows(cruise_data)