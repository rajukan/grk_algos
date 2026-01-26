'''

Input [11111] => Output 1
Input [123152] => Output 4, rem we are taking about substrings not subsequences

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right=1
        n=len(list(s))
        left=0
        max_len=1
        bag=[s[left]]

        while right<n:
            if s[left]!= s[right] and s[right] not in bag:
                bag.append(s[right])
                max_len=max(len(bag),max_len)
            else:
                left=right
                bag.clear()
                bag.append(s[left])
            right+=1
        print(max_len)
        print(bag)
        return max_len



if __name__=='__main__':
    t=Solution()
    t.lengthOfLongestSubstring("123512")
    # t.lengthOfLongestSubstring("1234129012345")
