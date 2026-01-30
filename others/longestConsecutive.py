from typing import List

'''
Given 

input [1,2,4,8,9,11,10,13,12] output 6
input [100,4,200,1,3,2] output 4
input [1,1,1,3] output 1


'''

class Solution:
    def longest_consecutive(self, nums:List[int]) -> int:
        max_len = 0

        for num in nums:

            if (num -1) not in nums: #Starting point
                length =1
                while (num + length) in nums:
                    length +=1

                max_len = max(max_len,length)

        print(max_len)
        return max_len


if __name__ == "__main__":
    s = Solution()
    s.longest_consecutive([11,1,3,1,1,1,12,14,13,15,16])