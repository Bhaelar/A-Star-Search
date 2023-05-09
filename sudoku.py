class Sudoku:
    def __init__(self, puzzle) -> None:
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.columns = len(puzzle[0])

    def is_puzzle_valid(self) -> bool:
        """
        Checks if the puzzle to be solved is valid and solvable

        Returns
        -------
        Boolean
            True: if the value is valid
            False: If the value is not valid
        """
        for row in range(self.rows):
            for col in range(self.columns):
                cell_value = self.puzzle[row][col]
                if cell_value not in range(10):
                    return False
                if cell_value != 0:
                    if (
                        self._is_value_valid_in_row_full_puzzle(row, cell_value) == False
                        or self._is_value_valid_in_column_full_puzzle(col, cell_value) == False
                        or self._is_value_valid_in_square_full_puzzle(row, col, cell_value == False)
                    ):
                        return False
        return True

    def _is_value_valid_in_row(self, row, value) -> bool:
        """
        Checks if a potential value to be inserted in the board is valid in provided row

        Parameters
        ----------
        row: Integer
            The index of the row
        value: Integer
            The value to be inserted

        Returns
        -------
        Boolean
            True: if the value is valid
            False: If the value is not valid
        """
        for col in range(self.columns):
            if value == self.puzzle[row][col]:
                return False
        return True

    def _is_value_valid_in_row_full_puzzle(self, row, value) -> bool:
        """
        Checks if a value in a row in a non-empty sudoku puzzle is legal

        Parameters
        ----------
        row: Integer
            The index of the row
        value: Integer
            The value to be inserted

        Returns
        -------
        Boolean
            True: if the value is valid
            False: If the value is not valid
        """
        count = 0
        for col in range(self.columns):
            if value == self.puzzle[row][col]:
                count += 1
                if count > 1:
                    return False
        return True

    def _is_value_valid_in_column(self, column, value) -> bool:
        """
        Checks if a potential value to be inserted in the board is valid in provided column

        Parameters
        ----------
        column: Integer
            The index of the column
        value: Integer
            The value to be inserted

        Returns
        -------
        Boolean
            True: if the value is valid
            False: If the value is not valid
        """
        for row in range(self.rows):
            if value == self.puzzle[row][column]:
                return False
        return True

    def _is_value_valid_in_column_full_puzzle(self, column, value) -> bool:
        """
        Checks if a value in a column in a non-empty sudoku puzzle is legal

        Parameters
        ----------
        row: Integer
            The index of the row
        value: Integer
            The value to be inserted

        Returns
        -------
        Boolean
            True: if the value is valid
            False: If the value is not valid
        """
        count = 0
        for row in range(self.rows):
            if value == self.puzzle[row][column]:
                count += 1
                if count > 1:
                    return False
        return True

    def _is_value_valid_in_square(self, row, column, value) -> bool:
        """
        Checks if a potential value to be inserted in the board is valid in its square

        Parameters
        ----------
        row: Integer
            The index of the row
        column: Integer
            The index of the column
        value: Integer
            The value to be inserted

        Returns
        -------
        Boolean
            True: if the value is valid
            False: If the value is not valid
        """
        square_row_start = (row // 3) * 3
        square_column_start = (column // 3) * 3

        for row_idx in range(square_row_start, square_row_start + 3):
            for col_idx in range(square_column_start, square_column_start + 3):
                if value == self.puzzle[row_idx][col_idx]:
                    return False
        return True

    def _is_value_valid_in_square_full_puzzle(self, row, column, value) -> bool:
        """
        Checks if a value in a square in a non-empty sudoku puzzle is legal

        Parameters
        ----------
        row: Integer
            The index of the row
        value: Integer
            The value to be inserted

        Returns
        -------
        Boolean
            True: if the value is valid
            False: If the value is not valid
        """
        count = 0
        square_row_start = (row // 3) * 3
        square_column_start = (column // 3) * 3

        for row_idx in range(square_row_start, square_row_start + 3):
            for col_idx in range(square_column_start, square_column_start + 3):
                if value == self.puzzle[row_idx][col_idx]:
                    count += 1
                    if count > 1:
                        return False
        return True

    def _is_solved(self) -> bool:
        """
        Checks if the sudoku puzzle is solved

        Returns
        -------
        Boolean
            True: if the value is valid
            False: If the value is not valid
        """
        for row in range(self.rows):
            for col in range(self.columns):
                cell = self.puzzle[row][col]
                if (
                    cell == 0
                    or self._is_value_valid_in_row_full_puzzle(row, cell) == False
                    or self._is_value_valid_in_column_full_puzzle(col, cell) == False
                    or self._is_value_valid_in_square_full_puzzle(row, col, cell)
                    == False
                ):
                    return False
        return True

    def get_empty_cells(self) -> list:
        """
        Returns a list of the indices of empty cells in the puzzle

        Returns
        -------
        list
            A list containing lists which consist of row and col
        """
        empty_cells = []
        for row in range(self.rows):
            for col in range(self.columns):
                if self.puzzle[row][col] == 0:
                    empty_cells.append([row, col])
        return empty_cells

    def get_candidates_for_empty_cell(self, row, col) -> list:
        """
        Checks for the candidate values of an empty cell on the board

        Parameters
        ----------
        row: Integer
            The index of the row
        col: Integer
            The index of the column

        Returns
        -------
        list
            list of integer values
        """
        candidates = []
        for i in range(10):
            if (
                self._is_value_valid_in_row(row, i)
                and self._is_value_valid_in_column(col, i)
                and self._is_value_valid_in_square(row, col, i)
            ):
                candidates.append(i)
        return candidates

    def print_board(self):
        """
        Prints the sudoku board in a pretty format
        """
        print()
        for i in range(9):
            if i in [3, 6]:
                print("----------+-----------+----------")
            for j in range(9):
                if j in [3, 6]:
                    print(" | ", end="")
                print(f" {self.puzzle[i][j]} ", end="")
            print()
