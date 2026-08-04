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

def max_subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    current = nums[0]
    for n in nums[1:]:
        current = max(n, current + n)  # extend, or restart at n
        max_sum = max(max_sum, current)
    return max_sum

arr = [-5,5,1,2,-30,4,5,4]
print(max_subarray(arr))
