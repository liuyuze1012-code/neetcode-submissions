# this method uses iterative BFS
# the logic is the same where we go through the entire grid until we see a one and we mark all nearby '1' 
# as zero
# this time we use BFS to find the nearby '1'
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            while q:
                i, j = q.popleft()
                if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                    continue
                grid[i][j] = '0'
                q.append((i, j + 1))
                q.append((i + 1, j))
                q.append((i, j - 1))
                q.append((i - 1, j))

        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    bfs(r, c)
        return num_islands
