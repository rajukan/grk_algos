from typing import List


class Solution:
    #Hashing mechanism
    def longest_consecutive(self, nums:List[int]) -> int:
        max_len = 0
        nums=set(nums)

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
    s.longest_consecutive([1,2,4,8,9,11,10,13,12])