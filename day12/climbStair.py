def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    a = 1
    b = 2
    current = 0
    for i in range (3, n+1):
        current = a + b
        a = b
        b = current
    return current
print(climbStairs(0, 5))