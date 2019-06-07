import re

pattern = r"eggs"

if re.match(pattern, "venkieggseggsvenkieggsvenkai"):
    print('Match Found')

else:
    print('No Match Found')

if re.search(pattern, "eggsvenkieggsvenkieggsvenkai"):
    print('Match Found')
else:
    print('No Match Found')


print(re.findall(pattern, "eggsvenkieggsvenkieggsvenkai"))