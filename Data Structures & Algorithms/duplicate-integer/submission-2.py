class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) != len(set(nums)):
        #     return True
        # else:
        #     return False

        hs = set()
        for i in nums:
            if i in hs:
                return True
            hs.add(i)
        return False

        
       
        