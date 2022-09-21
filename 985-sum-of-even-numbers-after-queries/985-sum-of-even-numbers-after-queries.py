# class Solution:
#     def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         arr = []
#         for i,j in zip(queries,nums):
#             nums[i[1]] = nums[i[1]] + i[0]
#             suma=0
#             for a in range(len(nums)):
#                 if nums[a]%2 == 0:
#                     suma+=nums[a]
#             arr.append(suma)
#         return arr

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(v for v in nums if v % 2 == 0)
        res: list[int] = []

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            
            nums[idx] += val
            
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            
            res.append(even_sum)
        
        return res