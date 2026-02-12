'''
PROBLEM: TWO SUM II - INPUT ARRAY IS SORTED

DESCRIPTION: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

 Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

EXAMPLES:

Example 1: Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2: Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Two-pointer scan ⇒ requires sorted input
Hash map two-sum ⇒ works on unsorted input
'''


def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    #Invariant: pointers move monotonically toward each other or forward once.
    #Idea: sum too small → move left; too big → move right.
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1


'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

[1,2,3,4,_,_,_,_]
'''

def removeDuplicates(nums: list[int]) -> int:
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return nums

'''
Squares of a Sorted Array

Input: sorted array (can include negatives)
Output: sorted squares

Invariant: largest square is always at one of the ends
'''

def sortedSquares(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [0] * n
    left, right = 0, n - 1
    write = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res[write] = nums[left] ** 2
            left += 1
        else:
            res[write] = nums[right] ** 2
            right -= 1
        write -= 1

    print(res)



if __name__ == "__main__":
    # print(twoSum([2,7,11,15],9))
    # print(twoSum([2,3,4,5,9,11],6))
    # print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    sortedSquares([-2,-1,3,4,-6])