# Time Complexity: O(NlogN)
# Space Complextiy O(N)
# where N is the number of elements in `changed` 
class Solution:
    def findOriginalArray(self, changed):
        # use Counter to count the frequency of each element in `changed`
        cnt, ans = Counter(changed), []
        # if the length of the input is odd, then return []
        # because doubled array must have even length
        if len(changed) % 2: return []
        # sort in ascending order
        for x in sorted(changed):
            print(x)
            # if the number of cnt[x] is greater than than cnt[x * 2]
            # then there would be some cnt[x] left
            # therefore, return [] here as changed is not a doubled array
            if cnt[x] > cnt[x * 2]: return []
            # handle cases like [0,0,0,0]
            if x == 0:
                # similarly, odd length -> return []
                if cnt[x] % 2:
                    return []
                else: 
                    # add `0` `cnt[x] // 2` times 
                    ans += [0] * (cnt[x] // 2)
            else:
                # otherwise, we put the element `x` `cnt[x]` times to ans
                ans += [x] * cnt[x]
            cnt[2 * x] -= cnt[x]
            # reset cnt[x] to 0
            # think about the case like [2,1,2,4,2,4]
            cnt[x] = 0
        return ans