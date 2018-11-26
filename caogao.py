import os
txt = open('readme.md', 'r')
lines = txt.readlines()
for line in lines:
    if line[0] == '|' and "#" not in line and "---" not in line:
        name = line.split('|')[1]
        file = open('src/{}/{}.py'.format(name, name), 'w')
        file.close()
