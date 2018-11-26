class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        perameter = 0
        landlist = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    perameter += 4
                    landlist.append((x, y))
        for land in landlist:
            perameter = perameter-neighbourLand(grid, land[0], land[1])
        return perameter


def neighbourLand(grid, x, y):
    count = 0
    if x-1 >= 0:
        if grid[x-1][y] == 1:
            count += 1
    if x+1 <= len(grid)-1:
        if grid[x+1][y] == 1:
            count += 1
    if y-1 >= 0:
        if grid[x][y-1] == 1:
            count += 1
    if y+1 <= len(grid[x])-1:
        if grid[x][y+1] == 1:
            count += 1
    return count


if __name__ == "__main__":
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print Solution().islandPerimeter(grid)
