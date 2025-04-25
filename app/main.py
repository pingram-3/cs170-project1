from .heuristics import *
from .astar import *


def main():
    # change n to change the dimensions of the grid
    n = 3
    #  this is the default puzzle grid, the user can choose a different puzzle if they want
    puzzle_grid = [
        [1, 2, 3],
        [4, 8, 0],
        [7, 6, 5],
    ]

    # Prompt user input
    print(
        'Welcome to nha023 and ____ 8 puzzle solver. Type “1” to use a default puzzle, or “2” to enter your own puzzle.'
    )
    user_choice = int(input())

    if (user_choice == 1):
        print('Using default puzzle grid...')
    elif (user_choice == 2):
        print('Enter your puzzle, use a zero to represent the blank')
        puzzle_grid = []
        # builds puzzle grid from input
        for i in range(n):
            user_input = input(
                f'Enter row {i + 1}, use space or tabs between numbers '
            ).split()
            if (len(user_input) != n):
                print(
                    f'Invalid row size of {len(user_input)}, expected: {n}. Terminating program.'
                )
                return
            temp_row = [int(num) for num in user_input]
            puzzle_grid.append(temp_row)
    else:
        print('Invalid choice, terminating program')
        return

    # outputs the stored puzzle for testing purposes
    print('Your puzzle is:')
    for row in puzzle_grid:
        print(row)

    print('Enter the number for your choice of algorithm:')
    print('(1) Uniform Cost Search')
    print('(2) A* with the Misplaced Tile heuristic.')
    print('(3) A* with the Euclidean distance heuristic.')
    user_choice = int(input())

    if (user_choice == 1):
        # uniform cost search
        zero = lambda grid : 0
        A_star(puzzle_grid, zero)
    elif (user_choice == 2):
        A_star(puzzle_grid, heuristic_misplaced_tile)
        pass
    elif (user_choice == 3):
        A_star(puzzle_grid, heuristic_euclidean_distance)
        pass
    else:
        print('Invalid choice, terminating program')
        return


if __name__ == "__main__":
    main()
