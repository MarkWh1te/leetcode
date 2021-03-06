// 64. Minimum Path Sum

// Given a m x n grid filled with non-negative numbers,
//  find a path from top left to bottom right
//  which minimizes the sum of all numbers along its path.

// Note: You can only move either down or right at any point in time.

// Example:

// Input:
// [
//   [1,3,1],
//   [1,5,1],
//   [4,2,1]
// ]
// Output: 7
// Explanation: Because the path 1→3→1→1→1 minimizes the sum

#include <vector>
#include <iostream>
using namespace std;

class Solution
{
  public:
    int minPathSum(vector<vector<int>> &grid)
    {
        return walk(grid, 0, 0);
    }
    int walk(vector<vector<int>> &grid, int i, int j)
    {
        if ((i == grid.size() - 1) && (j == grid[0].size() - 1))
        {
            return grid[i][j];
        }
        if (i == grid.size() - 1)
        {
            return walk(grid, i, j + 1) + grid[i][j];
        }
        if (j == grid[0].size() - 1)
        {
            return walk(grid, i + 1, j) + grid[i][j];
        }
        return min(walk(grid, i + 1, j), walk(grid, i, j + 1)) + grid[i][j];
    }
};

int main()
{
    vector<vector<int>> test = {
        {1, 3, 1},
        {1, 5, 1},
        {4, 2, 1}};
    Solution s = Solution();
    int answer = s.minPathSum(test);
    cout << answer << endl;
    return 0;
}