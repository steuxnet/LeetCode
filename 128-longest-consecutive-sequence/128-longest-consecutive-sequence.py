class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
	    s = set(nums)
	    max_length = 0

	    for n in nums:
		    if n-1 not in s: #// ensure n is the lowest number of a consecutive sequence
			    curr_length = 1 

			    while n+1 in s: #// extend current consec. seq.
				    n += 1
				    curr_length += 1

			    max_length = max(max_length, curr_length) #// update maximum length

	    return max_length