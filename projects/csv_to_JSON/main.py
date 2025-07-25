import os
import csv
import json


CSV_FILE = "csv_data.csv"
JSON_FILE = "json_data.json"


def load_csv_file(filename):
    if not os.path.exists(filename):
        return []
        print("No Data Found in CSV FILE")

    with open(filename,"r",encoding="utf-8") as f:
        return list(csv.DictReader(f))  
    
def save_data(data,filename):
    if not data:
        print("There is no data in csv file")
        return

    with open(filename,"w",newline="",encoding="utf-8") as f:
        json.dump(data,f,indent=2)   
        print(f"{len(data)} records added! ")             

def main():
    data = load_csv_file(CSV_FILE)
    save_data(data,JSON_FILE)

if __name__ == "__main__":
    main()
