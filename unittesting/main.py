import re
def sayHello(name):
    try:
        if re.match(r"[A-Za-z]{3,}$",name):
            return name
        else:
            return "enter falid name !"
    except TypeError as err:
        print("Enter a name ",err)

print(sayHello("am"))