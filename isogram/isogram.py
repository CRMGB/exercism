  
def is_isogram(string):
    justChar = list(''.join(e for e in string if e.isalnum()).lower())
    noRepeat = dict.fromkeys(justChar)
    return len(justChar) == len(noRepeat)

##Exercism solution:
    # def is_isogram(string):
    #     characters_lower = [c.lower() for c in string if c.isalpha()]
    #     return len(set(characters_lower)) == len(characters_lower)
