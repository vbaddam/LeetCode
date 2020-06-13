class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if k == -1:
                nums1[:j+1] = nums2[:j+1]
                return nums1
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                k = k - 1
                j = j - 1
                continue
            else:
                nums1[k] = nums1[i]
                k = k - 1
                i = i - 1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
