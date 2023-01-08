from utilities import generate_piece, print_board
import numpy

DEV_MODE = False


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    # TODO: generate a random piece and location using the generate_piece function
    dict_piece = generate_piece(game_board)
    # TODO: place the piece at the specified location
    row = dict_piece['row']
    col = dict_piece['column']
    game_board[row][col] = dict_piece['value']
    
    # Initialize game state trackers
    turn_counter = 0
    
    # Game Loop
    while True:
        # TODO: Reset user input variable
        
        # TODO: Take computer's turn
        if turn_counter % 2 == 0:
            
        # place a random piece on the board
            dict_piece = generate_piece(game_board)
            row = dict_piece['row']
            col = dict_piece['column']
            game_board[row][col] = dict_piece['value']
        
        # check to see if the game is over using the game_over function
            if game_over(game_board) == True:
                return False

        # TODO: Show updated board using the print_board function
            print_board(game_board)
            turn_counter += 1
        
        
        # TODO: Take user's turn
        if turn_counter % 2 == 1:
            
        # Take input until the user's move is a valid key
            valid_inputs = ['w','a','s','d','q']
            user_input = input()
            while user_input not in valid_inputs:
                user_input = input()
        # if the user quits the game, print Goodbye and stop the Game Loop
            if user_input == 'q':
                print('Goodbye')
                break
                
        # Execute the user's move
            if user_input == 'a':
                for row_index in range(len(game_board)):
                    vals_deleted = 0
                    while 0 in game_board[row_index]:
                        game_board[row_index].remove(0)
                        vals_deleted += 1
                    
                    for col_index in range(1,len(game_board[row_index])):
                        if game_board[row_index][col_index - 1] == game_board[row_index][col_index]:
                            game_board[row_index][col_index - 1] *= 2
                            game_board[row_index][col_index] = 0
                            
                    while 0 in game_board[row_index]:
                        game_board[row_index].remove(0)
                        vals_deleted += 1
                        
                    for x in range(vals_deleted):
                        game_board[row_index].append(0)
                        
            if user_input == 'd':
                for row_index in range(len(game_board)):
                    reversed_copy = game_board[row_index][::-1]
                    vals_deleted = 0
                    while 0 in reversed_copy:
                        reversed_copy.remove(0)
                        vals_deleted += 1
                    
                    for col_index in range(1,len(reversed_copy)):
                        if reversed_copy[col_index - 1] == reversed_copy[col_index]:
                            reversed_copy[col_index - 1] *= 2
                            reversed_copy[col_index] = 0
                            
                    while 0 in reversed_copy:
                        reversed_copy.remove(0)
                        vals_deleted += 1
                        
                    for x in range(vals_deleted):
                        reversed_copy.append(0)
                        
                    game_board[row_index] = reversed_copy[::-1]
            
            if user_input == 'w':
                new_board = numpy.transpose(game_board)
                new_board = new_board.tolist()
                
                for row_index in range(len(new_board)):
                    vals_deleted = 0
                    while 0 in new_board[row_index]:
                        new_board[row_index].remove(0)
                        vals_deleted += 1
                    
                    for col_index in range(1,len(new_board[row_index])):
                        if new_board[row_index][col_index - 1] == new_board[row_index][col_index]:
                            new_board[row_index][col_index - 1] *= 2
                            new_board[row_index][col_index] = 0
                            
                    while 0 in new_board[row_index]:
                        new_board[row_index].remove(0)
                        vals_deleted += 1
                        
                    for x in range(vals_deleted):
                        new_board[row_index].append(0)
                    
                game_board = numpy.transpose(new_board)
                game_board = game_board.tolist()
            
            if user_input == 's':
                new_board = numpy.transpose(game_board)
                new_board = new_board.tolist()
                
                for row_index in range(len(new_board)):
                    reversed_copy = new_board[row_index][::-1]
                    vals_deleted = 0
                    
                    while 0 in reversed_copy:
                        reversed_copy.remove(0)
                        vals_deleted += 1
                    
                    for col_index in range(1,len(reversed_copy)):
                        if reversed_copy[col_index - 1] == reversed_copy[col_index]:
                            reversed_copy[col_index - 1] *= 2
                            reversed_copy[col_index] = 0
                            
                    while 0 in reversed_copy:
                        reversed_copy.remove(0)
                        vals_deleted += 1
                        
                    for x in range(vals_deleted):
                        reversed_copy.append(0)
                        
                    new_board[row_index] = reversed_copy[::-1]
                    
                game_board = numpy.transpose(new_board)
                game_board = game_board.tolist()
                
            turn_counter += 1
        # Check if the user wins
            if game_over(game_board) == True:
                return False

    return game_board


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # TODO: Loop over the board and determine if the game is over
    for row in game_board:
        for col in row:
            if col == 2048:
                return True
                
    if (0 not in game_board[0]) and (0 not in game_board[1]) and (0 not in game_board[2]) and (0 not in game_board[3]): #when game_board is full
        # game_board =  [[2,2,2,2], [4,2,2,4], [2,2,2,2], [2,2,2,2]]
        # game_board =  [[2,4,2,2], [2,8,2,2], [2,2,2,32], [2,4,2,4]]
        for row_index in range(len(game_board)):
            for col_index in range(1,len(game_board[row_index])):
                if game_board[row_index][col_index - 1] == game_board[row_index][col_index]:
                    return False
        return True
    else:
        return False
    
                # TODO: Don't always return false


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
