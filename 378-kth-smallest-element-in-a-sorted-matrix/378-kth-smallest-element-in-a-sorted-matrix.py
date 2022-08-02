import bisect
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        low,high=matrix[0][0],matrix[n-1][n-1]
        ans=0
        while low<=high:
            mid=(low+high)>>1
            smallerElements=0
            for i in matrix:
                smallerElements+=bisect.bisect(i,mid)
            if smallerElements<k:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans