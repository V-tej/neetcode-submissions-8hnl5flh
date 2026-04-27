class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasset = set()

        for i in nums:
            if i in hasset:
                return True
            hasset.add(i)
        else:
            return False
        
        
       
        