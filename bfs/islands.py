'''

https://www.youtube.com/watch?v=pV2kpPD66nE

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


'''
from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        rows,cols = len(grid),len(grid[0])
        visit=set()
        islands=0

        def bfs(subgrid_row,subgrid_c):
            #remember bfs requires something like a deque
            q= deque()
            visit.add((subgrid_row,subgrid_c))
            q.append((subgrid_row,subgrid_c))
            #you can check 1 step in each direction, note, the origin is (0,0) and you take a step in all 4 directions
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    r, c = row+dr, col+dc

                    if ((r,c) not in visit and
                            r in range(rows) and #Boundary shields
                            c in range(cols) and
                            grid[r][c] == "1"):
                            q.append((r,c))
                            visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands

if __name__ == "__main__":
    s = Solution()
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(s.numIslands(grid))
