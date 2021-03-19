
my_file = open('text.txt','r')

def removeLines(file):
    file_lines = file.readlines()
    new_file = []
    new_line = ''
    i = 0
    print(file_lines)
    for line in file_lines:
        if line.count('\n') > 0:
            new_line = line.replace('\n',' ')
            new_file.append(new_line)
    return new_file


# print(lines)
def readCharNumber(file):
    i = 0
    file.seek(0)
    for f in file.read():
        if f == 'h' or f == 'H':
            i += 1
    return i

def readLines(lines):
    
    for line in lines:
        print(line)


print(readCharNumber(my_file))
readLines(my_file)
print(removeLines(my_file))