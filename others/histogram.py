'''
Problem

You're given an array of integers heights representing the heights of histogram bars, each of width 1, standing side by side. Find the area of the largest rectangle that can be formed within the histogram.

Sample Input

python
heights = [2, 1, 5, 6, 2, 3]
'''

heights = [2, 1, 5, 6, 2, 3]
heights = heights + [0]
n= len(heights)
count=0
stack=[]

max_ar = 0

for i in range(n):

    while stack and heights[i] < heights[stack[-1]]:
        bar_idx = stack.pop() #This bar just found its right wall
        '''
        stack is non-empty → after popping bar off, whatever's now on top of the stack (stack[-1]) is the 
        next-shorter bar to the left — that's the new left wall, by construction (remember, the stack only
         holds increasing heights, so the bar below bar must be shorter, meaning it correctly stopped bar's rectangle 
         from extending further left when bar was originally pushed).
        '''
        left_wall = stack[-1] if stack else  -1 
        width = i - left_wall -1
        max_ar = max(max_ar, width * heights[bar_idx])

    stack.append(i)






