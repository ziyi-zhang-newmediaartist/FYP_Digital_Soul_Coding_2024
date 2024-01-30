#  / \    / \
#  (   o\/o   )
#   \    |    /
#    \  ===  /
#     \____/

#Achievement: Read data from json file and feed them into ChatGPT

#1. Locate the JSON file within the user interface file.
#2. Input the content of the identified JSON file into CHATGPT.
#3. Generate a message based on the input and save it as a new version, such as Chair 2.0, along with attached version and timestamp information. (Ask ChaGPT to create a new Json file)

#--------------------------------LIBRARY-----------------------------------
import openai
import json
import os


#-----------------------------FILE INVENTORY--------------------------------
input_jsonfile = "/Users/morphini/Desktop/FYP/Coding/FYP_Digital_Soul_Coding_2024/ChaGPTinJson/input.json"
output_jsonfile = "/Users/morphini/Desktop/FYP/Coding/FYP_Digital_Soul_Coding_2024/ChaGPTinJson/output.json"
#-----------------------------FILE INVENTORY--------------------------------



#---------------------1. Locate the JSON file within the user interface file.
def locate_json_file(directory, keywords):
    # Iterate through files in the specified directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file contains any of the specified keywords
            if all(keyword.lower() in file.lower() for keyword in keywords):
                # Return the full path to the first matching file found
                return os.path.join(root, file)

    # If no matching file is found, return None
    return None

# Example Usage:
directory_path = '/Users/morphini/Desktop/FYP/Coding/FYP_Digital_Soul_Coding_2024/03JsonFiles'
search_keywords = ['chair']

found_json_file = locate_json_file(directory_path, search_keywords)

#if found_json_file:
    #print(f"JSON file found: {found_json_file}")
    # Now you can proceed with further actions, such as reading the content, etc.
#else:
    #print("No JSON file found.")


#---------------------2. cleanup the content ready for ChatGPT

json_file_path = found_json_file

def clean_and_print_json(json_file_path):
    # Read from the JSON file
    with open(json_file_path, 'r') as file:
        json_string = file.read()

    # Remove quotation marks, colons, and square brackets
    cleaned_json_string = json_string.replace('"', '').replace(':', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '')
    cleaned_data = cleaned_json_string.replace('\n', '').replace('    ', '')
    # Print the cleaned JSON-formatted string
    #print(cleaned_data)

clean_and_print_json(json_file_path)

cleaned_data_for_ChatGPT = clean_and_print_json(json_file_path)

#---------------------3. print the text into a Json file


# Set your OpenAI API key
openai.api_key = "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"

# Define the message you want to send to ChatGPT
user_message = "Please continue with the story. What will be happened to the item in the future, based on your own imagination:" + str(cleaned_data_for_ChatGPT)

# Make a request to the OpenAI API using the v1/chat/completions endpoint
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # You can use other chat models as well
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message},
    ],
)

# Get the generated response
chatgpt_message = response['choices'][0]['message']['content'].strip()

# Print or use the response
print(chatgpt_message)