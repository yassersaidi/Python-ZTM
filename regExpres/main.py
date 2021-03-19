import re as reg

string = "My Name is Yasser Saidi"
try:
    check = reg.search('Yasser',string)
    check2 = reg.compile('yasser')
    print(check.group())
    print(check2.findall(string))
except AttributeError as err:
    print("Dosn\'t exit")

