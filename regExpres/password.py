import re

string = "Hello world yasser"
print("hello" in string)

pattern = re.compile(r"(^[a-zA-Z0-9#$%&@]*{8,})")
password = "hgdsahdg54545"

print(re.match(password))

