import random, json

with open("config.json", "r") as file:
    output = file.read()
output = output.splitlines()
pairs = output[0].split(",")

dokeys=bool()
if output[-1] == "dokeys=True": dokeys=True
else: dokeys=False

vocabs=dict()

for pair in pairs:
    both = pair.split("-")#Gets the pairs
    vocabs[both[0]] = both[1] #because vocabs is a dict, i call that the first part of the pair equal the second one; 


if dokeys==True: first=list(vocabs.keys())
else: first=list(vocabs.values())

while True:
    whichwordn = random.randrange(0, len(vocabs))
    whichword = first[whichwordn]
    inp = input(f"Please tell me what {whichword} is in the other language: ")
    try: 
        if inp == vocabs[whichword]: print("thats right!")
    except:
        if inp == [k for k,v in vocabs.items() if v == whichword][0]: print("thats right!")
        else: print("thats wrong")

    

