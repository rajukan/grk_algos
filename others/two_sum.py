
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and YOU MAY NOT USE THE SAME ELEMENT TWICE.

You can return the answer in any order.

input:
nums = [2,7,11,15], target = 9
output: [0,1]

nums = [3,2,4,9,11], target = 6
output: [1,2]


'''


##Hash method
def two_sum(arr, target):
    index_map={}
    n=len(arr)

    for i in range(n):
        arr_num=arr[i]
        complement = target - arr_num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[arr_num] = i


print(two_sum([3,2,4,9,11], 11))