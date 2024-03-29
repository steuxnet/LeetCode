class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        waysToAdd = [0 for x in range(target+1)]
        waysToAdd[0] = 1
        
        for i in range(min(nums), target+1):
            waysToAdd[i] = sum(waysToAdd[i-num] for num in nums if i-num >= 0)
        
        return waysToAdd[-1]
            