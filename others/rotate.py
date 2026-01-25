'''

Given

nums=[1,2,3,4,5,6,7,8,9], k=3 , output [7, 8, 9, 1, 2, 3, 4, 5, 6]

nums=[-1,-100,3,99], k=2 , output [3,99,-1,-100]

'''

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        j=n-1

        while i <= j:
            nums[i],nums[j]=nums[j],nums[i]
            i +=1
            j -=1
        # 7,6,5,4,3,2,1
        #5,6,7,1,2,3,4

        i=0
        j=k-1
        while i <=j:
            nums[i],nums[j]=nums[j],nums[i]
            i +=1
            j -=1

        i=k
        j=n-1
        while i <=j:
            nums[i],nums[j]=nums[j],nums[i]
            i +=1
            j -=1

        print(nums)



if __name__ == '__main__':
    Solution().rotate(nums=[-1,-100,3,99], k=2)