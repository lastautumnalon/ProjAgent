from config import CONCLUDE_PROJECT_PROMPT



import yaml
from config import config_path
def read_config():
    with open(config_path,'r') as file:
        conf = yaml.safe_load(file)
    project_path = conf['Project']['path']
    return project_path

def write_config(project_path):
    conf = {
        'Project': {
            'path': project_path
        }
    }
    with open(config_path,'w') as file:
        yaml.safe_dump(conf,file)
    print("配置文件已更新。")

def is_code_file(file_path):
    # 定义代码文件的后缀名
    code_extensions = {
        '.html', '.css', '.js', '.ts', '.tsx',
        '.py', '.cpp', '.c', '.java', '.go',
        '.php', '.rb', '.swift', '.kt', '.rs'
    }
    # 获取文件的后缀名
    file_extension = file_path[file_path.rfind('.'):].lower()
    # 判断是否为代码文件
    return file_extension in code_extensions