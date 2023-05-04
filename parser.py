import os


def parse_txt_to_grid() -> list:
    """
    Reads the puzzle.txt file and returns a parsed list as a 9x9 grid

    Parameters
    ----------
    None


    Raises
    ------
    FileNotFoundError
    If the filename does not exist

    Returns
    -------
    list
        a 9 x 9 grid represented as a list
    """
    try:
        grid = []
        puzzle_txt_abs_path = os.path.abspath("puzzle.txt")
        with open(puzzle_txt_abs_path, "r", encoding="utf-8") as f:
            contents = f.readlines()
        for row in contents:
            new_row = [
                int(number.strip())
                for number in row
                if number != "\n" and number != " "
            ]
            grid.append(new_row)
        return grid
    except FileNotFoundError:
        return None
