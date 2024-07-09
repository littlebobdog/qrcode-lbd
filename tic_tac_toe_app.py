import streamlit as st

# Initialize game variables
current_player = 'X'
board = [''] * 9
game_over = False

# Function to check for a win
def check_win(player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for w in wins:
        if all(board[i] == player for i in w):
            return True
    return False

# Function to check for a draw
def check_draw():
    return all(cell != '' for cell in board)

# Function to reset the game
def reset_game():
    global board, current_player, game_over
    board = [''] * 9
    current_player = 'X'
    game_over = False

# Streamlit app
st.title('Tic-Tac-Toe Game')

# Main game loop
while not game_over:
    st.write(f"Current player: {current_player}")

    # Display the board
    st.write("   |   |   ")
    st.write(f" {board[0]} | {board[1]} | {board[2]} ")
    st.write("   |   |   ")
    st.write("-----------")
    st.write("   |   |   ")
    st.write(f" {board[3]} | {board[4]} | {board[5]} ")
    st.write("   |   |   ")
    st.write("-----------")
    st.write("   |   |   ")
    st.write(f" {board[6]} | {board[7]} | {board[8]} ")
    st.write("   |   |   ")

    # Player move input
    move = st.number_input(f"Player {current_player}, enter your move (1-9):", min_value=1, max_value=9, key=f'{current_player}_move')

    if st.button('Make Move'):
        if board[move - 1] == '':
            board[move - 1] = current_player
            if check_win(current_player):
                st.write(f"Player {current_player} wins!")
                game_over = True
            elif check_draw():
                st.write("It's a draw!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            st.write("Invalid move. Cell already occupied.")

    # Reset button
    if st.button('Reset Game'):
        reset_game()
        st.write("Game reset. Player X starts.")

