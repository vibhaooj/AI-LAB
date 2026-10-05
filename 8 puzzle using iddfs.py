goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def DLS(state, depth, visited):

    # Goal test
    if state == goal:
        print("Goal Found!")
        print_puzzle(state)
        return True

    # Depth limit reached
    if depth == 0:
        return False

    visited.add(state)

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0), # UP
        (1, 0), # DOWN
        (0, -1), # LEFT
        (0, 1) # RIGHT
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check valid move
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            new_state = tuple(new_state)

            if new_state not in visited:

                if DLS(new_state, depth - 1, visited):
                    return True

    return False


def IDDFS(start):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        visited = set()

        if DLS(start, depth, visited):
            return True

        depth += 1


# Main
print("Enter initial puzzle:")
initial = tuple(map(int, input().split()))

print("\nInitial State:")
print_puzzle(initial)

if IDDFS(initial):
    print("Solution found!")