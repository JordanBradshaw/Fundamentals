# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.
#
# Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.
def sudoku2(grid):
    def scanLines(index):
        hashTable = {}
        ##Horizontal
        for x in range(9):
            try:  # If the value does not = '.' try to get the key from the dictionary
                if grid[index][x] != ".":
                    hashTable[grid[index][x]] += 1
                    return False
            except KeyError:  # If it doesn't contain the key set the key = 1
                hashTable[grid[index][x]] = 1

        ##Vertical
        hashTable2 = {}
        for y in range(9):
            try:  # If the value does not = '.' try to get the key from the dictionary
                if grid[y][index] != ".":
                    hashTable2[grid[y][index]] += 1
                    return False
            except KeyError:  # If it doesn't contain the key set the key = 1
                hashTable2[grid[y][index]] = 1
        return True

    def scan3x3(x, y):
        hashTable = {}
        for n in range(3):
            for m in range(3):
                try:  # If the value does not = '.' try to get the key from the dictionary
                    if grid[y + n][x + m] != ".":
                        hashTable[grid[y + n][x + m]] += 1
                        return False
                except KeyError:  # If it doesn't contain the key set the key = 1
                    hashTable[grid[y + n][x + m]] = 1
        return True

    #### Scan 3x3 grids
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            if scan3x3(x, y) == False:
                print("3x3")
                return False
    #### Scan Lines grids
    for index in range(0, 9):
        if scanLines(index) == False:
            print("Lines")
            return False

    return True


grid = [
    ["7", ".", ".", ".", "4", ".", ".", ".", "."],
    [".", ".", ".", "8", "6", "5", ".", ".", "."],
    [".", "1", ".", "2", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "9", ".", ".", "."],
    [".", ".", ".", ".", "5", ".", "5", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]
print(sudoku2(grid))
