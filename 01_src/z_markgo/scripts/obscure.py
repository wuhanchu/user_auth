import requests,os

# 代码混淆
def change(path, output):
    with open(path, 'r') as f:
        str = f.read()
    url = 'http://pyob.oxyry.com/obfuscate'
    payload = {"append_source": "false",
               "preserve": "",
               "remove_docstrings": "true",
               "rename_nondefault_parameters": "true",
               "source": str}
    r = requests.post(url, json=payload)
    with open(output, 'w') as fp:
        fp.write(r.json()["dest"])


# 遍历目录（子目录），返回所有文件路径
def enum_path_files(path):
    path_len = len(path)
    file_paths = []
    if not os.path.isdir(path):
        print('Error:"', path, '" is not a directory or does not exist.')
        return
    list_dirs = os.walk(path)
    for root, dirs, files in list_dirs:
        for f in files:
            file_paths.append(os.path.join(root, f)[path_len + 1:])
    return file_paths


if __name__ == '__main__':
    path = r'.'  # 要混淆的文件位置

    file_paths = enum_path_files(path)
    for file in file_paths:
        if file.endswith(".py"):
            print("change: %s"%file)
            change(file,file)

print('finished!')
