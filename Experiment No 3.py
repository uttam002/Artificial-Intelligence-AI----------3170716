import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous_state=None):
        self.board = board
        self.moves = moves
        self.previous_state = previous_state
        self.empty_tile_position = self.find_empty_tile()

    def find_empty_tile(self):
        for row_index, row in enumerate(self.board):
            for col_index, value in enumerate(row):
                if value == 0:
                    return (row_index, col_index)
    
    def is_goal_state(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def generate_possible_moves(self):
        x, y = self.empty_tile_position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                yield self.create_new_state(new_x, new_y)

    def create_new_state(self, new_x, new_y):
        x, y = self.empty_tile_position
        new_board = [row[:] for row in self.board]  # Deep copy of the board
        new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]  # Swap tiles
        return PuzzleState(new_board, self.moves + 1, self)

    def calculate_manhattan_distance(self):
        """Heuristic function: Sum of the Manhattan distances of each tile from its goal position."""
        distance = 0
        for row_index, row in enumerate(self.board):
            for col_index, value in enumerate(row):
                if value != 0:
                    target_row = (value - 1) // 3
                    target_col = (value - 1) % 3
                    distance += abs(row_index - target_row) + abs(col_index - target_col)
        return distance

    def __lt__(self, other):
        """Comparison for priority queue, based on A* cost (moves + heuristic)."""
        return (self.moves + self.calculate_manhattan_distance()) < (other.moves + other.calculate_manhattan_distance())

def a_star_search(start_state):
    open_set = []
    heapq.heappush(open_set, start_state)
    visited_states = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal_state():
            return current_state
        
        visited_states.add(tuple(map(tuple, current_state.board)))

        for neighbor in current_state.generate_possible_moves():
            neighbor_board_tuple = tuple(map(tuple, neighbor.board))
            if neighbor_board_tuple not in visited_states:
                heapq.heappush(open_set, neighbor)
    
    return None

def print_solution_path(final_state):
    solution_path = []
    while final_state:
        solution_path.append(final_state.board)
        final_state = final_state.previous_state
    
    for step in reversed(solution_path):
        for row in step:
            print(row)
        print()  # Newline between steps

if __name__ == "__main__":
    initial_board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]  # Define starting board configuration
    start_state = PuzzleState(initial_board)
    solution = a_star_search(start_state)

    if solution:
        print("Solution found:")
        print_solution_path(solution)
    else:
        print("No solution found.")
