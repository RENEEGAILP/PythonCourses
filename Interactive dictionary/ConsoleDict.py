import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def GetDefinition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        closeMatch = get_close_matches(word, data.keys(), n=1, cutoff=0.8)
        if len(closeMatch):
            choice = input("Word not found. Did you mean %s ?Select 'y' for yes" % closeMatch[0])
            if choice.lower() == 'y':
                return data[closeMatch[0]]
            else:
                return "Word not found"
        else:
            return "Word not found"


word = input("Enter Word: ")
output = GetDefinition(word)

if isinstance(output, list):
    for val in output:
        print(val)
else:
    print(output)
