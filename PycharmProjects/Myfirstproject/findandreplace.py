import re

string = "This is venki & Hi am venki"
pattern = "venki"
newstring = re.sub(pattern, "rathod", string)

print(newstring)