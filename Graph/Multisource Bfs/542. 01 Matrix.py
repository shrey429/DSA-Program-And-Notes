# just same as "Rotten Oranges".
# only one extra we added here, the visited to check whether we have already visited the cell with value== 1 before or not.
# since the same cell can be visited again(in next cycle) and then time for that cell will increase.

# Note: First time we will see any '1' that will be shortest distance.

# Here we haveto find shortest distance of '1' from any of the '0' 
# so append all '0' into queue and apply multisource bfs.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col= len(mat), len(mat[0])
        visited= set()
        de= collections.deque([])
        time= 0
        count_1= 0
        for r in range(row):
            for c in range(col):
                if mat[r][c]== 0 :  # put all '0' into the Q
                    de.append((r, c))
                if mat[r][c]== 1:
                    count_1+= 1
        
        while de and count_1:
            time+= 1
            for i in range(len(de)):
                r, c= de.popleft()
                directions= [[r, c-1], [r, c+1], [r-1, c], [r+1, c]]  # left right, up, down
                for r1, c1 in directions:
                    if 0<= r1 < row and 0<= c1 < col and (r1, c1) not in visited and mat[r1][c1]== 1:
                        mat[r1][c1]= time
                        visited.add((r1, c1))
                        de.append((r1, c1))
                        count_1-= 1'
        return mat

# Java
"""
import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        boolean[][] visited = new boolean[rows][cols];
        Queue<int[]> queue = new LinkedList<>();
        int countOnes = 0;
        
        // Initialize the queue with all '0' cells and count '1' cells
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (mat[r][c] == 0) {
                    queue.offer(new int[] {r, c});
                    visited[r][c] = true;
                } else {
                    countOnes++;
                }
            }
        }

        int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        int time = 0;

        // Perform BFS to update the matrix
        while (!queue.isEmpty() && countOnes > 0) {
            time++;
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                int row = cell[0];
                int col = cell[1];

                for (int[] dir : directions) {
                    int newRow = row + dir[0];
                    int newCol = col + dir[1];

                    if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols 
                        && !visited[newRow][newCol] && mat[newRow][newCol] == 1) {
                        
                        mat[newRow][newCol] = time;
                        visited[newRow][newCol] = true;
                        queue.offer(new int[] {newRow, newCol});
                        countOnes--;
                    }
                }
            }
        }

        return mat;
    }
}
"""
