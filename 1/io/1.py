with open('C:\Windows\system.ini', 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉
