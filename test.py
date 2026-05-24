'''
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1



'''
from sqlalchemy.engine import row

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
# print(grid)


for i,row in enumerate(grid):
    for j,col in enumerate(row):
        print(f"{i=} {j=} {col=}",end=" ")

#
#
# if __name__ == '__main__':
#     # sub_arr_sum_k([1,2,4,3,0,2,1,5],3)
#     # sub_arr_sum_k([1,1,1],2)
#     # largent_contigous_arr([0,1,1,1,1,1,0,0,0])
#     print()
#





