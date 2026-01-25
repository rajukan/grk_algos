
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


'''


##Hash method
def two_sum(arr, target):
    index_map={}
    n=len(arr)

    for i in range(n):
        complement = target - arr[i]
        if complement in index_map:
            return [index_map[complement], i]
        index_map[arr[i]] = i

'''
5,2,4,1,7,11,12

9 - 5 = 4 {5 -> 0 }
9 - 2 = 7 {2 -> 1}
9 - 4 = 5 {0,2}

'''

print(two_sum([5,2,4,1,7,11,12], 9))