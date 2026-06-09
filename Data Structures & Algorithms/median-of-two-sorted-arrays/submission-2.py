class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        total = len(nums1) + len(nums2)
        half = total // 2
        
        l = 0
        r = len(nums1)
        
        while l <= r:
            i = l + (r - l) // 2 
            j = half - i          
            
            L1 = nums1[i - 1] if i > 0 else float('-inf')
            R1 = nums1[i] if i < len(nums1) else float('inf')
            L2 = nums2[j - 1] if j > 0 else float('-inf')
            R2 = nums2[j] if j < len(nums2) else float('inf')
            
            if L1 <= R2 and L2 <= R1:
                if total % 2:
                    return min(R1, R2)
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2
            elif L1 > R2:
                r = i - 1       
            else:
                l = i + 1