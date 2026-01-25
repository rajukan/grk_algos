'''

Input [11111] => Output 1
Input [123412] => Output 4

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right=1
        n=len(list(s))
        left=0
        max_len=1
        subarr=[s[left]]

        while right<n:
            if s[left]!= s[right] and s[right] not in subarr:
                subarr.append(s[right])
                max_len=max(len(subarr),max_len)
            else:
                left=right
                subarr.clear()
                subarr.append(s[left])
            right+=1
        print(max_len)
        print(subarr)
        return max_len



if __name__=='__main__':
    t=Solution()
    t.lengthOfLongestSubstring("123412")
    # t.lengthOfLongestSubstring("1234129012345")
