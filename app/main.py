from .tree import Node, Tree


def main():
    print("Hello from the main file")


if __name__ == "__main__":
    n = 3
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

    # logic to solve puzzle goes here
    if (user_choice == 1):
        # Uniform Cost Search code goes here
        pass
    elif (user_choice == 2):
        # A* with the Misplaced Tile heuristic code goes here
        pass
    elif (user_choice == 3):
        # A* with the Euclidean distance heuristic code goes here
        pass
    else:
        print('Invalid choice, terminating program')
        return