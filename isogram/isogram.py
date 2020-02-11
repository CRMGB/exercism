  
def is_isogram(string):
    justChar = list(''.join(e for e in string if e.isalnum()).lower())
    noRepeat = dict.fromkeys(justChar)
    if(len(justChar) != len(noRepeat)):
        return False
    return True
