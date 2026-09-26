

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

n=len(height)
max_arr=0

left=0
right=n-1

while left < right:
    width = right - left
    if height[left] < height[right]:
        max_arr = max(max_arr, height[left] * width)
        left+=1
    else:
        max_arr = max(max_arr, height[right] * width)
        right-=1

print(max_arr)


