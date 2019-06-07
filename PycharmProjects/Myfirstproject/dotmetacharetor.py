import re

pattern = r"gr.@..com"

if re.match(pattern, "gra@v.com"):
    print("Match found")
else:
    print("Match not found")