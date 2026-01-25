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

def max_sum_subarray(arr):

    result = max_sum = arr[0]
    for pointer in range(1, len(arr)):
        ar_sum = max_sum + arr[pointer]
        max_sum = max(ar_sum, arr[pointer])
        result = max(max_sum, result)

    return result

arr = [-5,5,1,2,-30,4,5,4]
print(max_sum_subarray(arr))
