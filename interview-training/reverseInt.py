import typing

def reverse(self, x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    isNegative = False
    y = 0
    if (x < 0):
        isNegative = True
        x = x * -1
    while (x > 0):
        lastDigit = x % 10
        y = y*10 + lastDigit
        x = x // 10
        if (y > INT_MAX or y < INT_MIN):
            return 0
    print(y)
    if (isNegative):
        x = y * -1
    else:
        x = y
        
    
    return x
print(reverse(0, 123))	