from openai import OpenAI
import os
client = OpenAI(
    api_key="",# use your own api key
)


command='''
#chat history
'''

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system", "content":"You are a person named Ayush who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Ayush skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)