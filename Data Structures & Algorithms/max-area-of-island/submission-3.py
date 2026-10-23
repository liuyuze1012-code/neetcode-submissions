class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Use DFS to find the area of one block: start at one block
        # go in 4 possible directions if next block is 1, then continue and count += 1
        # if no then stop

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or c == COLS or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
            return(1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        
        area = 0
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = dfs(r, c)
                max_area = max(area, max_area)
        
        return max_area



        