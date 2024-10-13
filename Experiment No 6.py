def minimax(board, depth, is_maximizing):
    """
    Minimax function to choose the best move for Tic-Tac-Toe
    Arguments:
    - board: Current game state
    - depth: Current depth in the game tree
    - is_maximizing: Boolean indicating if we are maximizing or minimizing the score
    """
    # Base conditions: Check if there is a winner
    if check_winner(board, 'X'):
        return 1  # X wins
    elif check_winner(board, 'O'):
        return -1  # O wins
    elif is_board_full(board):
        return 0  # Draw
    
    # Maximizing player's turn (X)
    if is_maximizing:
        best_score = -float('inf')  # Initialize best score to a very low value
        for move in get_possible_moves(board):
            # Simulate the move
            board = make_move(board, move, 'X')
            score = minimax(board, depth + 1, False)  # Recursive minimax call
            board = undo_move(board, move)  # Undo the move after simulation
            best_score = max(score, best_score)  # Choose the maximum score
        return best_score
    else:
        # Minimizing player's turn (O)
        best_score = float('inf')  # Initialize best score to a very high value
        for move in get_possible_moves(board):
            board = make_move(board, move, 'O')
            score = minimax(board, depth + 1, True)  # Recursive minimax call
            board = undo_move(board, move)
            best_score = min(score, best_score)  # Choose the minimum score
        return best_score
