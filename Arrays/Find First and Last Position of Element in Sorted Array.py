class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = [i for i in range(len(nums)) if target == nums[i]]
        if a == []:
            return([-1,-1])
        else:
            return(a[0],a[-1])
