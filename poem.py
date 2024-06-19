def poem(x,y):
    pNoun = x.title()
    adj = y.lower()

    print(f"{pNoun} are red, violets are blue")
    print(f"Monty Python is {adj}, woo hoo!")

pNoun = input("Please enter a plural noun: ")
adj = input("Please enter an adjective: ")

poem(pNoun,adj)