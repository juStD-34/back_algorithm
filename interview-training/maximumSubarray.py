class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        min = 0
        max = nums[0]
        for i in range(0, len(nums)):
            if (nums[i] - min > max):
                max = nums[i] - min
            if (nums[i] < min):
                min = nums[i]
        return max
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        