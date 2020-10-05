def write_array(text, file_name):
    file_name.writelines(text)
    return

file = open(r'C:\Users\79821\FilesForGit\1.txt', 'r')
array = []
for line in file:
    array.append(line)
file.close()
output = open(r'C:\Users\79821\FilesForGit\2.txt', 'w')
write_array(array, output)
output.close()
