phonebook = {"Chris": "555-1111", "Katie": "555-2222", "Joanne": "555-3333"}

"""
print(phonebook)
print(len(phonebook))
"""

"""
CREATING A DICTIONARY WITH DICT

mydictionary = dict(m=8, n=9)
print(mydictionary)
"""

"""
CALLING AN ITEM IN THE DICTIONARY

phonebook = {"Chris": "555-1111", "Katie": "555-2222", "Joanne": "555-3333"}
phone = phonebook["Chris"]
print(phone)

name = "Chris"
if name in phonebook:
    print(phonebook[name])
else:
    print("Not Found")
"""

"""
EDITING A DICTIONARY

phonebook["Chris"] = "555-4444"
phonebook["Joe"] = "555-0123"
print(phonebook)
"""

"""
REMOVING THINGS FROM A DICTIONARY. DELETES KEY AND VALUE.

del phonebook["Chris"]
print(phonebook)
"""

"""
ITERATE THROUGH KEYS. K IS THE ITERATOR

for k in phonebook:
    print(phonebook[k])
"""

"""
ITERATE THROUGH VALUES

for v in phonebook.values():
    print(v)
"""

"""
ITERATE THROUGH BOTH KEY AND VALUE PAIR WITH ITEMS METHOD. WHEN YOU USE ITEMS, YOU GET BOTH THE KEY AND THE VALUE. THE PARANTHASES THAT ARE RETURNED ARE A TUPLE. 

for pair in phonebook.items():
    print(pair)

IF YOU DON'T WANT A TUPLE TO BE RETURNED:

for k,v in phonebook.items():
    print(k,v)
"""

"""
METHODS

CLEAR. WIPES DICTIONARY. 

GET METHOD. THE GET METHOD IS UNIQUE BECAUSE YOU CAN SPECIFY A DEFAULT VALUE, WHICH IS WHAT RETURNED IF PYTHON DOESN'T FIND THE KEY IN THE DICTIONARY. 
ITS AN ERROR AVOIDING TECHNIQUE. 

KEYS. RETURNS ALL THE DICTIONARIES IN A SEQUENCE.

POP. RETURNS THE VALUE ASSOCIATED WITH THE SPECIFIED KEY AND THEN REMOVES THAT KEY-VALUE PAIR FROM THE DICTIONARY. 
THINK OF IT AS YOU ARE POPPING THE ITEM OUT OF THE DICTIONARY.
"""
