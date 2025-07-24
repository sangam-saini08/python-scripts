import os
import json
import csv


INPUT_FILE = "data.json"
OUTPUT_FILE = "converted_data.csv"


def laod_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file is not found")
        return []
    
    with open(filename,"r",encoding="utf_8")as f:

        try:
            return json.load(f)
        except:
            print("invalid json format")


def convert_to_csv(data,filename):
    if not data:
        print("No data found")

    fields = list(data[0].keys())        

    with open(filename,"w",newline="",encoding="utf-8")   as f:
        writer = csv.DictWriter(f,fieldnames=fields)
        writer.writeheader()
        for record in data:
            writer.writerow(record)
        print(f"converted {len(data)} records to csv")


def main():
    data = laod_json_data(INPUT_FILE)                    
    convert_to_csv(data,OUTPUT_FILE)

if __name__ == "__main__":
    main()