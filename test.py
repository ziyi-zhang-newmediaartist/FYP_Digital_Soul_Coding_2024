# Load the JSON data from the file
import json

input_jsonfile = "C:/Users/fyp/Documents/GitHub/FYP_Digital_Soul_Coding_2024/03JsonFiles/1.json"

with open(input_jsonfile) as f:
    data = json.load(f)

# Retrieve the value of the "abstract" attribute
abstract = data["Basics"]["abstract"]

print(abstract)