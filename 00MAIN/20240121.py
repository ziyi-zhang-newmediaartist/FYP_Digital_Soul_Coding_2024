import openai
import json

input_jsonfile = "/Users/morphini/Desktop/FYP/Coding/FYP_Digital_Soul_Coding_2024/ChaGPTinJson/input.json"
output_jsonfile = "/Users/morphini/Desktop/FYP/Coding/FYP_Digital_Soul_Coding_2024/ChaGPTinJson/output.json"

# Set your OpenAI API key
openai.api_key = "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"

# Read the input from the JSON file
with open(input_jsonfile, 'r') as file:
    input_data = json.load(file)

# Convert the JSON object to a string
input_string = json.dumps(input_data)

# Make a request to the OpenAI API using the correct endpoint
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": input_data["text"]}
    ]
)

# Extract relevant information
model_reply = response['choices'][0]['message']['content']

# Create a dictionary with the information you want to save
output_data = {
    "input": input_data,
    "model_reply": model_reply
}

# Convert the dictionary to a JSON string
output_json_string = json.dumps(output_data, indent=2)

# Write the JSON string to a file
with open(output_jsonfile, 'w') as file:
    file.write(output_json_string)

# Print the model's reply
print(model_reply)