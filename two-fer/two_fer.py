def two_fer(name):
    if name:
        return "One for " + name +", one for me."
    else: 
        return "One for you, one for me." 
    pass
#Exercism solution:
#def two_fer(name=None):
    #return "One for {}, one for me.".format(name or 'you')