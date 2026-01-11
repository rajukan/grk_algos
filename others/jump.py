
'''

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


'''

def check_jump(nums):
    n = len(nums)

    i =0
    jump=False

    while i < n:
        numb=nums[i]
        if numb + i == nums[n-1]:
            jump = True
            break
        i+=1
    print(jump)

'''
i=0, numb=n[0]=2, 4
1,3 = 4, 4 true

i=0,numb=3, 4
1,2,
2,1,
3,0
4


'''

if __name__ == '__main__':
    check_jump([2,3,1,1,4])
