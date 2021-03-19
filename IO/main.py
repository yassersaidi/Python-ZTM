my_file = open('text.txt','r+')

def removeLines(file):
    file_lines = file.readlines()
    new_file = []
    new_line = ''
    print(file_lines)
    for line in file_lines:
        if line.count('\n') > 0:
            new_line = line.replace('\n','&nbsp')
            new_file.append(new_line)
    file.writelines(new_file)
    return file
print(removeLines(my_file).readlines())
my_file.close()

