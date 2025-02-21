from config import CONCLUDE_CODE_PROMPT,CONCLUDE_PROJECT_PROMPT
from config import config_path
from helper import read_config,write_config,is_code_file
import os
from llm import chat
import tqdm
from pathlib import Path

def get_all_files(path):
    file_list = []
    for path in Path(path).rglob('*'):
        if path.is_file():
            file_list.append(str(path))
    return file_list

def conclude_code(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        content = file.read()
    response = chat(CONCLUDE_CODE_PROMPT,content)
    return file_path + '\n' + response


if __name__ == '__main__':
    project_path = ''
    if os.path.exists(config_path):
        project_path = read_config()
        print("已读取配置文件,项目地址：",project_path)
    else:
        project_path = write_config(input("请输入项目地址："))

    print("项目代码文件如下：")
    file_list = get_all_files(project_path) # 目录下所有文件
    code_files = [file for file in file_list if is_code_file(file)] # 目录下代码文件
    for file in code_files:
        print(file)

    # 1.总结每部分的代码
    code_conclusions = []
    for file in tqdm.tqdm(code_files,desc='Concluding project code...'):
        conclusion = conclude_code(file)
        code_conclusions.append({'file':file,'conclusion':conclusion})

    print(code_conclusions)

    # 2.分析工程结构
    code_conclusions = [f"文件地址：{i['file']}\n该文件的功能和接口：{i['conclusion']}" for i in code_conclusions]
    project_struct = chat(CONCLUDE_PROJECT_PROMPT,'\n'.join(code_conclusions))
    print(project_struct)
