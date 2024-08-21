from boards import boards_archive

DEFAULT_BOARD_DATE = "21-08-2024"


def is_safe(board, row, col, board_size):

    # check if a queen is in the same column as the given cell
    for i in range(board_size):
        if board[i][col] == "Q":
            return False

    # do the same check but for row
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # check diagonal
    if row > 0 and col > 0 and board[row - 1][col - 1] == "Q":
        return False
    if row > 0 and col < board_size - 1 and board[row - 1][col + 1] == "Q":
        return False
    if row < board_size - 1 and col > 0 and board[row + 1][col - 1] == "Q":
        return False
    if row < board_size - 1 and col < board_size - 1 and board[row + 1][col + 1] == "Q":
        return False

    return True


def check_colour_regions(board, size, regions):
    colour_counts = {}
    for row in range(size):
        for col in range(size):
            if regions[row][col] not in colour_counts:
                colour_counts[regions[row][col]] = 0
            if board[row][col] == "Q":
                colour_counts[regions[row][col]] += 1

    for _, count in colour_counts.items():
        # only one queen allowed per region
        if count > 1:
            return False
    return True


def solveLinkedInQueens(board, row, board_size, regions):
    # recursive backtracking algorithm
    if row >= board_size:
        return check_colour_regions(board, board_size, regions)

    for col in range(board_size):
        if is_safe(board, row, col, board_size):
            board[row][col] = "Q"
            if solveLinkedInQueens(board, row + 1, board_size, regions):
                return True
            # if no solution exists with this move, undo and retry a new move
            board[row][col] = "0"
    return False


def print_board(board):
    for row in board:
        print(' '.join(row))


if __name__ == "__main__":
    board_date = "19-08-2024"

    try:
        board_colours = boards_archive[board_date]
    except KeyError:
        print(f"Board for that date not archived, defaulting to {
              DEFAULT_BOARD_DATE}")
        board_colours = boards_archive[DEFAULT_BOARD_DATE]

    board_size = len(board_colours)
    board = [['0' for _ in range(board_size)] for _ in range(board_size)]

    solveLinkedInQueens(board, 0, board_size, board_colours)

    print_board(board)
