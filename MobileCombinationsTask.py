def combinations(digits):
    dig_char= {'2': 'abc', 
        '3':'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7':'qprs',
        '8':'tuv',
        '9':'wxyz'}
    
    if len(digits)==0:
        return []
    elif len(digits)>4:
        error="Number of input digits too big!"
        return error
       
    nbr= list(dig_char[digits[0]])
        
    for digit in digits[1:]:
        nbr = [i+j for i in nbr for j in list (dig_char[digit])]
    return nbr

x = combinations("")
y = combinations("23")
z = combinations("25555")
print (x)
print (y)
print (z)
