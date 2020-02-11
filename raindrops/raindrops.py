def convert(number):
    listReturn = []
    if number % 3 == 0:
        listReturn.append("Pling")
    if number % 5 == 0:
        listReturn.append("Plang")
    if number % 7 == 0:
        listReturn.append("Plong")
    if len(listReturn) == 0:
        listReturn.append(str(number))
    return "".join(listReturn) 
    pass
#exercism result
# def convert(number):
#     """
#     Converts a number to a string according to the raindrop sounds.
#     """
  
#     result = ''
#     if number % 3 == 0:
#         result += 'Pling'
#     if number % 5 == 0:
#         result += 'Plang'
#     if number % 7 == 0:
#         result += 'Plong'

#     if not result:
#         result = str(number)
#     return result
