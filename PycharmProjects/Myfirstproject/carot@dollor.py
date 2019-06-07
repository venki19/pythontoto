import re

pattern = "^gr.y$"

if re.match(pattern, "grey"):
    print("Match found")