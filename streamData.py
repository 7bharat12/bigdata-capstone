# -*- coding: utf-8 -*-
"""
Created on Wed May 24 22:43:03 2023

@author: bharat
"""

import boto3
import csv
import json

region = 'us-east-1'
stream_name = 'capstone-kinesis'
csv_file_path = r'C:\Users\bhara\Desktop\BharatChandra_BigData_Capstone\yellow.csv'

# Create a Kinesis client
kinesis_client = boto3.client('kinesis', region_name=region)

with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(row),
            PartitionKey=row['tpep_pickup_datetime']
        )
        print(f"Record sent to Kinesis: {response['SequenceNumber']}")
