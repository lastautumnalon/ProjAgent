from ollama import Client
from tagdel import remove_code_blocks,remove_think_tags
client = Client(
    host='http://localhost:11434'
)
import re


def chat(prompt:str,content:str)->str:
    response = client.chat(model='deepseek-r1',messages=[
        {'role':'system','content':prompt},
        {'role':'user', 'content':content}
    ],
    options={
        'temperature':0.0
    })
    return remove_code_blocks(remove_think_tags(response['message']['content']))

if __name__ == '__main__':
    print(chat('根据用户输入的文本生成代码，注意只需要输出代码','1+1'))