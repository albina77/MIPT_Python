import zipfile
import os

def f(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

file = zipfile.ZipFile(r"C:\Users\79821\Downloads\main.zip")
file.extractall(r"C:\Users\79821\FilesForGit")
answer = []

for folder, subfolders, files in os.walk(r"C:\Users\79821\FilesForGit"):
    for file in files:
        if file.endswith('.py'):
            answer.append(folder)
answer = f(answer)
Answer = []
for item in answer:
    k = 0
    for i in range(len(item)):
        if item[i] == "\\":
            k = i
    item = item[(k+1):] + "\n"
    Answer.append(item)
Answer.sort()
print(Answer)
output = open(r'C:\Users\79821\FilesForGit\With_py.txt', 'w')
output.writelines(Answer)