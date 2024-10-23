def sortKeys(dict):
    return dict['num']

def countWords(c):
    count = 0
    for i in c.split():
        count += 1
    
    return count


def formatMessage(dl):
    print(f'--Begin Book Report on {b.name}.--')
    print(f'{countWords(contents)} words found in the document')
    print("\n")

    for i in dl:
        print(f"The '{i['letter']}' character was found {i['num']} times.")

    print("\n--End Message--")
    

with open("books/frankenstein.txt") as b:
    contents = b.read()
    charCount = 0
    countDict = {}
    dictList = []
    
from string import ascii_lowercase as alc

for i in alc:
    countDict = {}
    charCount = 0

    for c in contents.lower():
        if c == i:
            charCount += 1
    countDict["letter"] = i
    countDict["num"] = charCount
    dictList.append(countDict)
        
dictList.sort(reverse=True, key=sortKeys)

formatMessage(dictList)