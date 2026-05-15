'''

Given
rotate array by k steps
nums=[1,2,3,4,5,6,7,8,9], k=3 , output [7, 8, 9, 1, 2, 3, 4, 5, 6]

nums=[-1,-100,3,99], k=2 , output [3,99,-1,-100]

'''

class Solution:

    def rotate(self, nums: list[int], k: int) -> None:

        n = len(nums)
        # k = k % n
        #Observe method within method
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Reverse entire array
        reverse(0, n - 1)

        # Reverse first k elements
        reverse(0, k - 1)

        # Reverse remaining elements
        reverse(k, n - 1)

        print(nums)


if __name__ == '__main__':
    Solution().rotate(nums=[-1,-100,3,99], k=2)