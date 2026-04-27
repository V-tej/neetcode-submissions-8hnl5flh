class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count_max = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            count_max = max(nums[i], count_max+nums[i])
            max_sum = max(max_sum,count_max)
        return max_sum
         