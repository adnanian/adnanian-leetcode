from math import factorial

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Use combinatorics without repetition to fill all spaces
        # in the triangle.
        base_factorial: int = factorial(rowIndex)
        fact_down: int = int(base_factorial / rowIndex) if rowIndex > 0 else 1
        fact_up: int = 1
        # (n, r) = n!/(r!(n-r)!)
        row: List[int] = [1] * (rowIndex + 1)
        index: int = 1
        midpoint: float = len(row) / 2
        while index < midpoint:
            value = int(round(base_factorial / (fact_up * fact_down)))
            row[index] = value
            row[len(row) - 1 - index] = value
            fact_down = int(fact_down/(rowIndex - index))
            fact_up *= (index + 1)
            index += 1
        return row
