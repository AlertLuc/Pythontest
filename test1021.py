# File and data formatting
"""
stdin（Standard input file）
stdout（Standard output file）
stderr（Standard error file）
"""
import sys

file = sys.stdout
file.write("hello")

# open(file, mode='r',encoding="utf-8", buffering=1)
"""
file.close()
Automatically shut down
with open('a.txt') as f:
        pass
"""
"""
Read all the data in the file
read(n=-1) read()
"""
with open('file.txt', mode='r') as f:
    print(f.read(2))
    print(f.read())

# Controls the number of rows to read
with open('file.txt', mode='r', encoding='utf-8') as f:
    print(f.readlines(-1))

string = "Here we are all, by day; by night."
with open('write_file.txt', mode='w', encoding='utf-8') as f:
    size = f.write(string)
    print(size)

string = "Here we are all, by day;\nby night we're hurl'd By dreams, " \
         "each one into a several world."
with open('write_file.txt', mode='w', encoding='utf-8') as f:
    f.writelines(string)

# tell()：Gets the current read/write location of the file
# seek()：Controls file read and write locations
with open('file.txt') as f:
    print(f.tell())
    print(f.read(5))
    print(f.tell())

with open('file.txt') as f:
    print(f.tell())
    loc = f.seek(5, 0)
    print(loc)

with open('file.txt', 'rb') as f:
    f.seek(5, 0)
    f.seek(3, 1)

"""
os.remove(The file name)
os.rename(old,new)
os.mkdir(Directory name)/os.rmdir(Directory name)
os.getcwd()
os.chdir(Directory name) Changes
os.listdir(Directory） obtain
"""

csv_file = open('score.csv')
lines = []
for line in csv_file:
    line = line.replace('\n', '')
    lines.append(line.split(','))
print(lines)
csv_file.close()

for line in lines:
    print(line)
    file.write(','.join(line)+'\n')
csv_file.close()
file.close()

import json
py_obj = [[1, 2, 3], 345, 23.12, 'qwe', {'key1':(1,2,3), 'key2': (2, 3, 4)}, True, False, None]
json_str = json.dumps(py_obj)
print(json_str)
py_data = json.loads(json_str)
print(py_data)


