import random

pp=[
    ["je","ich"],
    ["tu","du"],
    ["il/elle","er/sie"],
    ["nous","wir"],
    ["vous","ihr"],
    ["ils/elles","sie"],
]

verbs=[
    [
        ["ai","habe"],
        ["as","hast"],
        ["a","hat"],
        ["avons","haben"],
        ["avez","habt"],
        ["ont","haben"]
    ],
    [
        ["suis","bin"],
        ["es","bist"],
        ["est","ist"],
        ["sommes","sind"],
        ["êtes","seid"],
        ["sont","sind"],
    ],
    [
        ["parle","rede"],
        ["parles","redest"],
        ["parle","redet"],
        ["parlons","reden"],
        ["parlez","redet"],
        ["parlent","reden"],
    ]

]
    #vorlage
    # {
    #     "",""],
    #     "",""],
    #     "",""],
    #     "",""],
    #     "",""],
    #     "",""],
    # }



while True:
    whichverb_N=random.randrange(0,len(verbs))
    verb = verbs[whichverb_N]#verb which gets used
    pronoun_N = random.randrange(0,len(pp))#randomly generates which pronoun to use for that verb-> for conjugation
    pronoun = pp[pronoun_N]#gives the pronoun list which has the pronoun in both french and german
    verb = verb[pronoun_N]#..but with the verb

    inp = input(f"What is '{pronoun[1]} {verb[1]}' in french? \n")
    inpList = inp.split()
    inpPronoun=inpList[0]
    inpVerb=inpList[1]
    if inpPronoun==pronoun[0] and inpVerb==verb[0]: print("You did it! good boy!")
    else: print(f"Wrong, it was actually '{pronoun[0]} {verb[0]}'")