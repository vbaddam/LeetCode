
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        f = set()
        for i in range(len(nums)-2):
            a = nums[i]
            ind = set()
            for j in range(i+1, len(nums)):
                b = nums[j]
                c = -a-b
                if b not in ind:
                    ind.add(c)
                else:
                    f.add((a,b,c))
        return(map(list, f))
        '''
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        triplets = set()
        for i in range(n-2):
            a = nums[i]
            index = set()
            for j in range(i+1, n):
                b = nums[j]
                c = -a-b
                if b not in index:
                    index.add(c)
                else:
                    triplets.add((a,b,c))
        return map(list, triplets)
        '''
