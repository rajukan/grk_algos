class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bag=set()
        left=0
        n=len(s)
        max_len=0

        for right in range(n):
            if s[right] not in bag:
                bag.add(s[right])
                max_len = max(max_len,right-left+1)
            else:
                while s[right] in bag:
                    bag.remove(s[left])
                    left +=1
                bag.add(s[right])

            return max_len

