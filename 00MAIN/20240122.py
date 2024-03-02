#
#                `           '
#                 `         '
#                  :       :
# ___              `       '              ___
# `Y8888ba.         :     :         .ad8888P'
#   88888888b.      `     '      .d88888888
#   8888888888b.     :   :     .d8888888888
#   88888P'  `?8b.   `   '   .d8P'  `?88888
#   88888       "8b   : :   d8"       88888
#  j88888  .db.   ?b       dP   .db.  88888k
#    `888  8888    `b ( ) d'    8888  888'
#     888. ?88P                 ?88P .888
#     8888  ""        / \        ""  8888
#     8888b.   _,aaY' | | `Yaa,_   .d8888
#    j8888888888f"'   \ /    `"?888888888k
#       88888'.'      d b       `.`8888
#       88' .8       d' `b       8. `88
#       f  .88 db   d'| |`b   db 88.  l
#          888 `'   8 | | 8   `' 88b
#          888      8 | | 8      888
#         d888b   .d8 \_/ 8b.   d888b
#         88888888888     88888888888
#         8888888888       8888888888
#         f 8888888'       `8888888 l
#           `888888         888888'
#            8P  `Y         Y'  ?8
#            8                   8
#            f                   l
#

#DIGITAL SOUL







#--------------------------------LIBRARY-----------------------------------
import openai
import json
import os
from datetime import datetime


#-----------------------------FILE INVENTORY--------------------------------
input_jsonfile = "C:/Users/fyp/Documents/GitHub/FYP_Digital_Soul_Coding_2024/ChaGPTinJson/input.json"
output_jsonfile = "C:/Users/fyp/Documents/GitHub/FYP_Digital_Soul_Coding_2024/ChaGPTinJson/output.json"
#

#---------------------READ KEY WORDS FROM USER INTERFACE--------------------
user_input_01 = input("Enter the first keyword: ")
user_input_02 = input("Enter the second keyword: ")


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
directory_path = 'C:/Users/fyp/Documents/GitHub/FYP_Digital_Soul_Coding_2024/03JsonFiles'
search_keywords_01 = [user_input_01]
search_keywords_02 = [user_input_02]

found_json_file_01 = locate_json_file(directory_path, search_keywords_01)
found_json_file_02 = locate_json_file(directory_path, search_keywords_02)

if found_json_file_01:
    print(f"JSON file found: {found_json_file_01}")
else:
    print("No JSON file found.")

if found_json_file_02:
    print(f"JSON file found: {found_json_file_02}")
else:
    print("No JSON file found.")


#---------------------2. cleanup the content ready for ChatGPT

json_file_path_01 = found_json_file_01
json_file_path_02 = found_json_file_02


with open(json_file_path_01, 'r') as json_file:
    json_string = json_file.read()

cleaned_json_string_01 = json_string.replace('"', '').replace(':', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '')
cleaned_data_02 = cleaned_json_string_01.replace('\n', '').replace('    ', '')

cleaned_data_for_ChatGPT_01 = str(cleaned_data_02)
#print(cleaned_data_for_ChatGPT_01)


with open(json_file_path_02, 'r') as json_file:
    json_string = json_file.read()

cleaned_json_string_02 = json_string.replace('"', '').replace(':', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '')
cleaned_data_02 = cleaned_json_string_02.replace('\n', '').replace('    ', '')

cleaned_data_for_ChatGPT_02 = str(cleaned_data_02)
#print(cleaned_data_for_ChatGPT_02)


#---------------------3. print the text into a Json file


# Set your OpenAI API key
openai.api_key = "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"

# Define the message you want to send to ChatGPT
user_message = "create a new story based on the following 2 elements: the element 1 is" + cleaned_data_for_ChatGPT_01 + ", the element 2 is" + cleaned_data_for_ChatGPT_02
#"and store the above Combined story in a json file, with attributions of what, why, when, who, where, how. The answer should contains json file only, without other texts"

# Make a request to the OpenAI API using the v1/chat/completions endpoint
response = openai.ChatCompletion.create(
    model="gpt-4",  # You can use other chat models as well
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message},
    ],
)

# Get the generated response
chatgpt_message = response['choices'][0]['message']['content'].strip()

# Print or use the response
print(chatgpt_message)


#---------------------WRITE THE STORY INTO A JSON FILE, RENAME IT
# Information to be written to the JSON file
data = chatgpt_message

# Writing information to the new JSON file
#json_file_path = "/Users/morphini/Desktop/FYP/Coding/FYP_Digital_Soul_Coding_2024/00MAIN/output_user_interface.json"
#with open(json_file_path, 'w') as file:
#    json.dump(data, file, indent=4)

# Get the current timestamp
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create a file name with the timestamp
json_file_path = f"C:/Users/fyp/Documents/GitHub/FYP_Digital_Soul_Coding_2024/00MAIN/{current_time}.json"

# Writing information to the JSON file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)


