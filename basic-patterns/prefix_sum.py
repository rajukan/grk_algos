'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals k.
Example:

Input: nums = [1,5,2,4,12], k = 6
Output: 2 (The subarrays are [1,5] and [2,4])

'''
from collections import defaultdict


def subarray_sum(nums,k):
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1
    prefix_sum=0
    count=0

    for num in nums:
        prefix_sum+=num
        print(f"{prefix_sum=}")
        print(prefix_counts)
        count += prefix_counts.get(prefix_sum-k,0)
        print(count)
        prefix_counts[prefix_sum] +=1

    print(count)
    print(prefix_counts)
    return count




# subarray_sum([1,5,6,2,4,3,3,9],6)

'''
Input: nums = [0,1]


Output: 2 (The subarray [0,1] has equal 0s and 1s.)


Input: nums = [0,1,0]


Output: 2 (Subarrays [0,1] or [1,0] have equal 0s and 1s.)


'''

def zerone(nums):
    n=len(nums)
    count=0
    presum=0
    cntmap=defaultdict(int)
    cntmap[0]=1

    new_nums = [-1 if num == 0 else num for num in nums  ]

    for num in new_nums:
        presum+=num
        count+=cntmap.get(presum,0)
        cntmap[presum] +=1


    print(count)
    print(cntmap)
    return count

zerone([0,1,0,0,1])
