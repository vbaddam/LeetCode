class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snum = sorted(nums)
        init = []
        if nums != snum:
            for i in range(len(nums)):
                if snum[i] != nums[i]:
                    init.append(i)
            return(init[-1] - init[0] + 1)
        else:
            return(0)
        
