def searchInsert(self, nums, target):
    start = 0;
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

print(searchInsert(0, [1,3,5,6], 5))