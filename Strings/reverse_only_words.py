# reverse only letters
import re

sentence = 'This is a test. More words! hahah:)'

temp_sentence = re.split(r'[?.,!;:()]', sentence)
print(temp_sentence)
queue = []

for i in sentence:
    if i in '?.,!;:()':
        queue.append(i)

res = ''
for line in temp_sentence:
    line = line.lstrip()
    line = line.split(' ')
    line = list(reversed(line))
    temp = ''
    for i in range(len(line)):
        print(line[i])
        if i == len(line)-1 and queue != [] and i>0:
            temp = temp + line[i] + queue.pop(0)+' '
        elif i == len(line)-1 and queue != [] and i==0:
            temp = temp + line[i] + queue.pop(0)
        else:
            temp = temp + line[i]+ ' '
        print(temp)

    res += temp
print(res)
    
