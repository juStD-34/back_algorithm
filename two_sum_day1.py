from typing import List


def twoSum(self, nums, target):
    numMap = {}
    n = len(nums)
    tr = True
    if (tr): 
        print(111)
    
    for i in range(n):
        numMap[nums[i]] = i
    print (numMap)
    
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
    
    return []
print(twoSum(0, [2,7,11,15], 9))
    