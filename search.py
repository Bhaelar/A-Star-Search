from sudoku import Sudoku


def a_star_search(puzzle, steps=0):
    """
    Applies A* star search recursively to solve a sudoku puzzle
    First, it fetches a list of empty cells present on the board
    Then, it computes the candidate values for each empty cell
    Then, following Most Constrained Variable Heuristic, it selects the cell with the least amount of candidates
    Then, it assigns the candidate value to the empty cell
    Calls the a_star_search recursively until the board is solved

    Parameters
    ----------
    puzzle: list
        A list containing the values of the sudoku board
    steps: Integer
        Number of steps taken to solve the sudoku puzzle

    Returns
    -------
    Boolean
        True: if a solution was found
        False: If a solution was not found
    """
    
    candidates = []
    board = Sudoku(puzzle)
    row = -1
    col = -1
    solved = False
    empty_cells = board.get_empty_cells()
    candidate_mappings = []

    for empty_cell in empty_cells:
        cell_candidate_mapping = {}
        candidates = board.get_candidates_for_empty_cell(empty_cell[0], empty_cell[1])
        cell_candidate_mapping[tuple(empty_cell)] = candidates
        candidate_mappings.append(cell_candidate_mapping)

    """
    Using most constrained value heuristic, we get the cells with the least number of possible values first
    """
    candidate_mappings.sort(key=lambda x: len(list(x.values())[0]))
    
    if len(candidate_mappings) > 0:
        candidates = candidate_mappings[0]
        key = list(candidates.keys())[0]
        row = key[0]
        col = key[1]
        value = list(candidates.values())[0]
        candidates = value

    if row < 0 and board._is_solved():
        solved = True
        print(f"Solved sudoku puzzle in {steps} steps")
    else:
        for i in range(len(candidates)):
            puzzle[row][col] = candidates[i]
            steps += 1
            if a_star_search(puzzle, steps):
                solved = True
                break
            puzzle[row][col] = 0
    return solved
