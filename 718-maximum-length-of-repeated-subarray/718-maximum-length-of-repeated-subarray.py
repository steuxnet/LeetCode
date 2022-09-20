class Solution:                 # 1) We build memo, a 2Darray, 2) iterate thru nums1 & nums2
                                # in reverse to populate memo, and then 3) find the max element
                                # in memo; its row and col in memo shows the starting indices
                                # for the common seq in nums1 and nums2.  

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1, n2 = len(nums1), len(nums2)          
        memo = [[0]*(n2+1) for _ in range(n1+1)]                    # <-- 1)
        
        for idx1 in range(n1)[::-1]:
            for idx2 in range(n2)[::-1]:
                
                if nums1[idx1] == nums2[idx2]:
                    memo[idx1][idx2] = 1 + memo[idx1+1][idx2+1]     # <-- 2)
       
        return max(chain(*memo))                           