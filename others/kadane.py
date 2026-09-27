'''

    Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
    Output: 11
    Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

    Input: arr[] = [-2, -4]
    Output: -2
    Explanation: The subarray [-2] has the largest sum -2.

    Input: arr[] = [5, 4, 1, 7, 8]
    Output: 25
    Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.
'''
nums = [2, 3, -8, 7, -1, 2, 3]
n=len(nums)
max_sum=curr_sum = nums[0]

for i in range(n):
    curr_sum = max(nums[i], curr_sum+nums[i])
    max_sum = max(max_sum,curr_sum)

print(max_sum)
