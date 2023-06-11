# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:45:32 2023

@author: bharat
"""

import json
import os
import re

input_folder = r'C:\Users\bhara\Desktop\BharatChandra_BigData_Capstone\DeliveryStreamOriginal'
output_folder = r'C:\Users\bhara\Desktop\BharatChandra_BigData_Capstone\DeliveryStreamJson'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over each file in the input folder
for filename in os.listdir(input_folder):
    input_file = os.path.join(input_folder, filename)
    output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.json")

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use regular expression to split the content into individual JSON objects
    pattern = r'({.*?})'
    objects = re.findall(pattern, content)
    
    # Process each JSON object and create a list of dictionaries
    data = []
    for obj in objects:
        item = json.loads(obj)
        data.append(item)

    # Write the formatted JSON to the output file
    with open(output_file, 'w') as file:
        file.write(json.dumps(data, indent=4))

print('JSON conversion completed for all files.')







