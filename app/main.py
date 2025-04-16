from .tree import Node, Tree


def main():
    # Prompt user input
    print("Enter a puzzle. The puzzle is an NxN grid of numbers.")
    print(
        "Separate numbers in a row with space, and separate rows by pressing enter."
    )
    user_input = input().split()

    # build puzzle grid from input
    temp_row = [num for num in user_input]
    n = len(temp_row)
    puzzle_grid = [temp_row]

    # gets the rest of the puzzle grid based on the size of the first row
    for _ in range(n - 1):
        user_input = input().split()
        temp_row = [num for num in user_input]
        puzzle_grid.append(temp_row)

    # outputs the stored puzzle for testing purposes
    print("Your puzzle is:")
    for row in puzzle_grid:
        print(" ".join(row))


if __name__ == "__main__":
    main()
