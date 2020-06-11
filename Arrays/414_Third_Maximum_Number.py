class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        snums = sorted(list(set(nums)), reverse = True)
        if len(nums) >= 3 and len(snums) >= 3:
            return(snums[2])
        else:
            return(snums[0])
