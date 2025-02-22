from config import MODULE_FIND_PROMPT,CODE_EDIT_PROMPT
from api_llm import chat
import json

def change(project_struct,code_files,code_conclusions):
    need = input("请输入您的功能需求：")
    print("正在查找要修改的模块...")
    response = chat(MODULE_FIND_PROMPT, f"项目架构：{project_struct}\n用户需求：{need}")
    print(response)
    found_modules = json.loads(response)
    print("Agent认为需要修改以下模块：\n", found_modules)
    input("Agent查找相关模块代码并进行分析修改...")
    modules = []
    # 根据模块名找路径
    for modstr in found_modules:
        for module in code_files:
            if modstr['mod'] in module:
                modules.append(module)
    print(f"找到模块路径:{'\t'.join(modules)}")

    for i,module in enumerate(modules):
        with open(module,'r') as file:
            code = file.read()
            resp = chat(CODE_EDIT_PROMPT,f"项目架构：{project_struct}\n"
                                  f"所有模块的接口：{code_conclusions}\n"
                                  f"用户需求：{need}\n"
                                  f"模块名称：{module}\n"
                                  f"模块代码：{code}\n"
                                  f"模块修改建议：{found_modules[i]['advice']}")
            print(f"模块：{module}\n"
                  f"修改前代码：{code}\n"
                  f"修改后代码：{resp}\n")
            opt = input("确认将修改覆盖到文件..(Y/N)")
            if opt == 'Y':
                with open(module,'w') as file:
                    file.write(resp)
                print(f"{module} 已写入.")
            input("回车后继续下一个模块..")