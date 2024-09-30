row_one = list(map(int, input().split()))
row_two = list(map(int, input().split()))
row_three = list(map(int, input().split()))
player_one_won = False
player_two_won = False

moves_done_player_one = 0
moves_done_layer_two = 0

for move in row_one:
    if move == 1:
        moves_done_player_one += 1
        if moves_done_player_one == 3:
            player_one_won = True
    elif move == 2:
        moves_done_layer_two += 1
        if moves_done_layer_two == 3:
            player_two_won = True
    elif move == 0:
        break

moves_done_player_one = 0
moves_done_layer_two = 0
for move in row_two:

    if move == 1:
        moves_done_player_one += 1
        if moves_done_player_one == 3:
            player_one_won = True
    elif move == 2:
        moves_done_layer_two += 1
        if moves_done_layer_two == 3:
            player_two_won = True
    elif move == 0:
        break

moves_done_player_one = 0
moves_done_layer_two = 0
for move in row_three:

    if move == 1:
        moves_done_player_one += 1
        if moves_done_player_one == 3:
            player_one_won = True
    elif move == 2:
        moves_done_layer_two += 1
        if moves_done_layer_two == 3:
            player_two_won = True
    elif move == 0:
        break
if row_one[0] == row_two[1] == row_three[2] == 1 or \
        row_one[2] == row_two[1] == row_three[0] == 1:
    player_one_won = True
elif row_one[0] == row_two[0] == row_three[0] == 1 or \
        row_one[1] == row_two[1] == row_three[1] == 1 or \
        row_one[2] == row_two[2] == row_three[2] == 1:
    player_one_won = True

if row_one[0] == row_two[1] == row_three[2] == 2 or \
        row_one[2] == row_two[1] == row_three[0] == 2:
    player_two_won = True
elif row_one[0] == row_two[0] == row_three[0] == 2 or \
        row_one[1] == row_two[1] == row_three[1] == 2 or \
        row_one[2] == row_two[2] == row_three[2] == 2:
    player_two_won = True

if player_one_won:
    print("First player won")
elif player_two_won:
    print("Second player won")
else:
    print("Draw!")