def removeDuplicates(self, nums):
    # i = 0
    # while i < len(nums) - 1:
    #     if nums[i] == nums[i + 1]:
    #         del nums[i]
    #     else:
    #         i += 1
    # return len(nums)
    count = 1
    for i in range( 1, len(nums)):
        if (nums[ i] != nums[i -1]):
            count += 1
    return count

print(removeDuplicates(0, [1,1,2]))