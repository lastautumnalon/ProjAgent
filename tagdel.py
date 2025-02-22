def remove_think_tags(text):
    # 使用正则表达式匹配并删除 <think>...</think> 及其内容
    clean_text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    return clean_text

def remove_code_blocks(text):
    # 匹配以 ```json 开头（不区分大小写和空格）和 ``` 结尾的块
    pattern = r'```\s*[a-ZA-Z0-9_-]*\s*([\s\S]*?)\s*```'
    # 替换为中间的内容（\1 表示第一个捕获组）
    return re.sub(pattern, r'\1', text, flags=re.IGNORECASE)