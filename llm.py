from ollama import Client

client = Client(
    host='http://localhost:11434'
)
import re
def remove_think_tags(text):
    # 使用正则表达式匹配并删除 <think>...</think> 及其内容
    clean_text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    return clean_text

def chat(prompt:str,content:str)->str:
    response = client.chat(model='deepseek-r1',messages=[
        {'role':'system','content':prompt},
        {'role':'user', 'content':content}
    ],
    options={
        'temperature':0.0
    })
    return remove_think_tags(response['message']['content'])

if __name__ == '__main__':
    print(chat('根据用户输入的文本生成代码，注意只需要输出代码','1+1'))