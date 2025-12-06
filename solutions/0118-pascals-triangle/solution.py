class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle: List[List[int]] = []
        for row in range(1, numRows + 1):
            match row:
                case 1:
                    pascal_triangle.append([1])
                case 2:
                    pascal_triangle.append([1,1])
                case _:
                    last_row: List[int] = pascal_triangle[row - 2]
                    # Subtract 2 to retrieve the last row index.
                    # Example: row = 3, means 2 rows were added,
                    # Meaning the last index is 1.
                    left: int = 0 # Left index for last row
                    right: int = 1 # Right index for last row
                    current_row: List[int] = [1]
                    # Loop through the previous row and add every pair of
                    # adjacent numbers togehter.
                    while left < len(last_row) - 1:
                        current_row.append(last_row[left] + last_row[right])
                        left += 1
                        right += 1
                    current_row.append(1)
                    pascal_triangle.append(current_row)
        return pascal_triangle
