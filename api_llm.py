from openai import OpenAI

from tagdel import remove_code_blocks,remove_think_tags

import re

from config import API_KEY

def chat(prompt:str,content:str)->str:
    client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[
        {'role':'system','content':prompt},
        {'role':'user', 'content':content}
    ],
    temperature=0.7,
    stream=False
    )
    return remove_code_blocks(remove_think_tags(response.choices[0].message.content))
