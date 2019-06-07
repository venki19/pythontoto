import re

patten = r"[A-Z][A-Z][0-9]"

if re.search(patten, "AA1"):
    print("Match Found")

metachar = r"eggs(becon)*"

if re.match(metachar,"eggsbeaconbecon"):
    print("Match found")

    # Gropus

test = r"eggs(becon)*eggs"

if re.match(test, "eggsbeconbeconeggs"):
    print("Match Found")