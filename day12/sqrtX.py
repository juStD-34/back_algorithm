def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    if x == 1:
        return 1
    left = 1
    right = x
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
print(mySqrt(0,12))