class Luhn:
    def __init__(self, card_num):
        if card_num.replace(" ", "").isdigit():
            #if the string contains just numbers make it a list of numbers and reverse it
            listNumbers = [int(i) for i in list(card_num.replace(" ", ""))[::-1]]
        else: 
            listNumbers = [0]
        double = [x * 2 for x in listNumbers[1::2]]
        newList = []
        for i in range(0, len(double)):
            #Using the ternary conditional operator
            newList.append(double[i] - 9) if double[i] > 9 else newList.append(double[i])
            
        #Get the minimum length of both lists and then double it to create the list.   
        num = min(len(listNumbers), len(newList))
        self.result = [None]*(num*2)
        #Undo the reverse list and then pass it to every over element, examp: [7, None, 5, None, 2, None, 6, None, 5, None, 1, None, 0, None, 3, None]
        self.result[::2] = newList[::-1][:num]
        self.result[1::2] = listNumbers[::2][::-1][:num]
        print("self.result[1::2]; ", self.result)
        # We cobine the two lists again for the ones that are odd or uneven
        self.result.extend(newList[::-1][num:])
        self.result.extend(listNumbers[::2][::-1][num:])
        print("self.result.extend; ", self.result)
            
    def valid(self):
        return True if sum(self.result) % 10 == 0 and self.result != [0] else False