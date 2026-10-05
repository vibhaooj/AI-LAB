# 8 Puzzle Problem using DFS

def dfs(start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        # Find the blank space (0)
        zero = state.index(0)
        row = zero // 3
        col = zero % 3

        # Possible moves: Up, Down, Left, Right
        moves = []

        if row > 0:
            moves.append(zero - 3)  # Up

        if row < 2:
            moves.append(zero + 3)  # Down

        if col > 0:
            moves.append(zero - 1)  # Left

        if col < 2:
            moves.append(zero + 1)  # Right

        for move in moves:
            new_state = list(state)

            # Swap blank with the selected tile
            new_state[zero], new_state[move] = \
                new_state[move], new_state[zero]

            stack.append((tuple(new_state), path + [state]))

    return None


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Initial state
start = (1, 0, 3,
         4, 2, 6,
         7, 5, 8)

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Solve using DFS
solution = dfs(start, goal)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for step, state in enumerate(solution):
        print("Step", step)
        print_puzzle(state)
else:
    print("No solution found.")
