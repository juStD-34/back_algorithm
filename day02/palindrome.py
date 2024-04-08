def isPalindrome(self, x):
    if x < 0:
        return False
    else: 
        strX = str(x)
        for i in range(0, len(strX)//2):
            if (strX[i] != strX[len(strX)-i-1]):
                return False
        return True
print(isPalindrome(0, -101))