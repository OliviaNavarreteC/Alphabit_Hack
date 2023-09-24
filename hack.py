import openai
import os
from dotenv import load_dotenv
datafull = []
 
def ask(arr):
    for element in arr:
        print(element)
        ask = input()
        datafull.append(element+" "+ask)
        



load_dotenv()
OPENAI_CHAT_MODEL_NAME = os.getenv("OPENAI_CHAT_MODEL_NAME")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY not found in .env file")

OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
if OPENAI_API_BASE is None:
    raise ValueError("OPENAI_API_BASE not found in .env file")

OPENAI_EMBEDDINGS_MODEL_NAME = os.getenv("OPENAI_EMBEDDINGS_MODEL_NAME")
if OPENAI_EMBEDDINGS_MODEL_NAME is None:
    raise ValueError("OPENAI_EMBEDDINGS_MODEL_NAME not found in .env file")

openai.api_type="azure"
openai.api_base= OPENAI_API_BASE
openai.api_version= "2023-07-01-preview"
openai.api_key = OPENAI_API_KEY
carrera = input("Enter your major \n")

prompt = "give me a set of questions, just 10 questions, to create a cv template for the " + carrera +" major as an array of strings. Only to copy and paste. Do not separate it by sections, dónt give further information. Ask for just 1 field per question"
message = dict(
    content = prompt,
    role = "user"
    )



    

completion = openai.ChatCompletion.create(engine=OPENAI_CHAT_MODEL_NAME,
messages=[message])

mess = completion.choices[0].message.content

#print(mess)

file_name = "cv.txt"
with open(file_name, 'w') as file:
    # Write the string to the file
    file.write(mess)


questions = []
with open(file_name, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Process each line as needed
       questions.append(line.strip())

ask(questions)

fullstr = "".join(datafull)
prompt2 = "give me a profesional cv for the " + carrera +" major based in this information only"+ fullstr + "use a simple reading format that is able to pass the first ai filter of selection from a company"
message = dict(
    content = prompt2,
    role = "user"
    )



    

completion = openai.ChatCompletion.create(engine=OPENAI_CHAT_MODEL_NAME,
messages=[message])

mess = completion.choices[0].message.content
print("------------------------------")


file_name = "cv.txt"
with open(file_name, 'w') as file:
    # Write the string to the file
    file.write(mess)
