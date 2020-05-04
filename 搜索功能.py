import os
import collections
disks = os.popen('fsutil fsinfo drives').read()
stack = []
for disk in disks:
    if '\u4e00' <= disk <= '\u9fff':
        continue
    elif disk.isalpha():
        diskName = disk + ":\\"
        # 压栈
        stack.append(diskName)
    else:
        continue

    while len(stack) != 0:
        dirPath = stack.pop()
        print(dirPath)
        filesList = os.listdir(dirPath)

        for fileNames in filesList:
            fileName = os.path.join(diskName, fileNames)
            if os.path.isdir(fileName):
                stat = []
                stat.append(fileName)
                a = stat.pop()
                special = "C:\Documents and Settings"
                if a == "C:\\Documents and Settings" or a == "C:\\Recovery" or a == "C:\\System Volume Information":
                    continue
                else:
                    filesLists = os.listdir(a)
                    print(a)

            else:
                pass
                # print("文件", fileName)