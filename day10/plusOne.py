def plusOne(self, digits):
    res = 0
    for i in range (0, len(digits)):
        res = res*10 + digits[i]
    res +=1
    list_of_digits = [int(i) for i in str(res)]

plusOne(0, [9,9])