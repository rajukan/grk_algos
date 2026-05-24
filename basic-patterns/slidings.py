

'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

'''

def minSubArrayLen(nums: list[int],target: int) -> int:
    left = 0
    curr_sum = 0
    max_len = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            max_len = min(max_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return 0 if max_len == float('inf') else max_len


'''

Input [1,1] => Output 1
Input [1,2,3,1,5,2] => Output 4, rem we are taking about substrings not subsequences

'''

def longest_substr(numlist):
    n=len(numlist)
    left=0
    max_len=0
    bucket=set()

    for right in range(n):
        while numlist[right] in bucket:
            #you do not reset, you repair it
            bucket.remove(numlist[left])
            left+=1
        bucket.add(numlist[right])
        max_len=max(max_len,len(bucket))
    print(max_len)

'''
Given array nums and integer k, return the maximum average of any subarray of length k.
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

'''

def findMaxAverage(nums: list[int], k: int) -> float:
    curr_sum = sum(nums[:k])
    best = curr_sum

    for i in range(k, len(nums)):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]
        best = max(best, curr_sum)

    print(f"{best/k}, {best=}")


if __name__ == "__main__":
    arr=[1,1]
    # longest_substr(arr)
    # print(minSubArrayLen([1,2,3,5,6], 7))
    findMaxAverage([1,12,-5,-6,50,3,0,0,0,1,10,0,48],4)