import json

# Step 1: Read the JSON file
json_file_path = '/Users/morphini/Desktop/FYP/Coding/FYP_Digital_Soul_Coding_2024/JsonFiles/Chair.json'
with open(json_file_path, 'r') as json_file:
    # Step 2: Extract the relevant information
    data = json.load(json_file)


# Create a dictionary with the information you want to save
output_data = data

# Convert the dictionary to a JSON string
output_json_string = json.dumps(output_data, indent=2)

paragraphed_output = "/Users/morphini/Desktop/FYP/Coding/FYP_Digital_Soul_Coding_2024/ChaGPTinJson/outparagraphed.json"

# Write the JSON string to a file
with open(paragraphed_output, 'w') as file:
    file.write(output_json_string)

# Print the model's reply
print(data)


