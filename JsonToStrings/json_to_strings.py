import json

file_path = '/Users/morphini/Desktop/FYP/Coding/FYP_Digital_Soul_Coding_2024/JsonToStrings/data.json'

# Read the content from the JSON file
with open('file_path', 'r') as file:
    data = json.load(file)

# Convert the data to a JSON-formatted string
json_string = json.dumps(data, indent=2)

# Print or use the JSON string as needed
print(json_string)
