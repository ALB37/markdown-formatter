import sys

path = sys.argv[1]
output = sys.argv[2]


file_to_edit = open(path, 'r')
file_to_write = open(output, 'w')

lines = file_to_edit.readlines()

for line in lines[:]:
    words = line.split(' ')
    accum = ''
    j = 0
    while (j < len(words)):
        while (j < len(words) and len(accum + ' ' + words[j]) < 80):
            if (words[j] == '\n'):
                j += 1
                continue
            accum = accum + ' ' + words[j]
            j += 1
        file_to_write.write(accum + '\n')
        accum = ''
