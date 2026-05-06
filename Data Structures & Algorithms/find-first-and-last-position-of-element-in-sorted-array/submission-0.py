class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.first_position(nums,target)
        second = self.second_position(nums,target)

        return [first,second]

    def first_position(self,nums,target):
        start = 0
        end = len(nums)-1
        ans = -1

        while start <= end:
            mid = (start+end)//2
            
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid -1
            else:
                ans = mid
                end = mid - 1
        return ans

    def second_position(self,nums,target):
        start = 0
        end = len(nums)-1
        ans = -1

        while start <= end:
            mid = (start+end)//2

            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                ans = mid
                start = mid + 1
        return ans