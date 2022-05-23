import json
from difflib import get_close_matches

elements = json.load(open("Python md\workbook\wordbook.json"))


def findmeaning(word):
    if word.lower() in elements:
        return elements[word.lower()]
    elif word.upper() in elements:
        return elements[word.upper()]
    elif word.title() in elements:
        return elements[word.title()]
    elif len(get_close_matches(word,elements.keys()))>0:
        closematches = get_close_matches(word,elements.keys())[0]
        user_decision = input("Do u mean %s instead[Y/N]" %closematches)
        user_decision = user_decision.lower()
        if user_decision =="y":
            return elements[get_close_matches(word,elements.keys())[0]]
        elif user_decision =="n":
            return "Cant Find Sorry"
        else:
            return "Sorry cant find"
    else:
        return "I cant find it check spelling mistake"

word = input("Enter the word:")

output =findmeaning(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)    
