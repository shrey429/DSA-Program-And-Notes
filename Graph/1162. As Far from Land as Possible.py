# just multisource bfs.

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        dq= collections.deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c]== 1:
                    dq.append((r, c))
        ans= 0
        while dq:
            ans+= 1
            for i in range(len(dq)):
                r,c = dq.popleft()
                directions= [[r, c-1],[r, c+1],[r-1, c], [r+1, c]]   # left, right, up, down
                for nr, nc in directions:
                    if 0<= nr< row and 0<= nc < col and grid[nr][nc]== 0:
                        dq.append((nr, nc))
                        grid[nr][nc]= 1   # simply marking as visited the zero we are visiting
        return ans -1 if (ans-1)!= 0 else -1 # since for 1st time we don't have to consider distance that's why 'ans-1'
                    
