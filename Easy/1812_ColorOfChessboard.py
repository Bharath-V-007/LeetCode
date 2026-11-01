class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col , row = coordinates[0] , coordinates[1]
        col_value = ord(col) - 96
        row_value = int(row)
        return abs(row_value - col_value)%2 == 1
