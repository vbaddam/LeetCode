class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        snums = sorted(nums)
        l = snums[-1]
        if len(nums) > 1:
            s = snums[-2]
            if l >= 2*s:
                for i in range(len(nums)):
                    if l == nums[i]:
                        return(i)
            else:
                return(-1)
        else:
            return(0)
        
