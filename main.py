from pprint import pprint

from parser import parse_txt_to_grid
from search import a_star_search
from sudoku import Sudoku

def main():
    """
        Calls the parser function and applies A* star search to the parsed sudoku grid
    """
    sudoku_grid = parse_txt_to_grid()
    
    if sudoku_grid is not None:
        if(a_star_search(sudoku_grid)):
            # pprint(sudoku_grid)
            Sudoku(sudoku_grid).print_board()
        else:
            print('Could not solve sudoku puzzle')
    else:
        print('Could not locate puzzle.txt file in the directory')

if __name__ == '__main__':
    main()