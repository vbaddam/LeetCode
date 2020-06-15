class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if target == nums[i]:
                    return(i)
        else:
            k = len(nums)
            for i in range(len(nums)):
                if i == 0 and target < nums[0]:
                    k = i
                elif target < nums[i] and target > nums[i-1]:
                    k = i
        return(k)
        
