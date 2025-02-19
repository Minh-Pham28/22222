from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, stop = 0, len(nums)-1 
        
        while start <= stop:
            mid = (start + stop) // 2

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                start = mid + 1
            else:
                stop = mid - 1
        
        return start
    
'''        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
'''


sol = Solution()
nums = [1,3,5,6]
target = 5
print (f'{nums} -> {sol.searchInsert(nums, target)}')

