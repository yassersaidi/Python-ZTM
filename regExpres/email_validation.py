import re

check_email = re.compile("here dir reg nta3k jibha mn google hh")

email = "here sdir reg nta3k jibha mn google hh"
if (check_email.match(email)):
    print("Good email!")
else:
    print("try another email") 