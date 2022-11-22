import random
# based on https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/
# little update

class game:
    options = ['Rock', 'Scissors', 'Paper']


    def __init__(self):
        game.play_game(self)

    def play_game(self):
        print("TIE IS NOT POSSIBLE!\n")
        player_points = 0
        comp_points = 0
        while True:
            comp_move = game.options[random.randint(0, 2)]
            if player_points >= 3 or comp_points >= 3 and player_points>comp_points:
                print('PLAYER WON')
                print(f'END OF GAME \nComputer:{comp_points}, Human: {player_points}')
                break
            if player_points >= 3 or comp_points >= 3 and player_points<comp_points:
                print('COMPUTER WON')
                print(f'END OF GAME \n Computer:{comp_points}, Human: {player_points}')
                break

            print('YOUR MOVE:')
            player_move = input("Rock, Paper, Scissors?\n")
            print(f'Computer move: {comp_move}')

            if player_move == comp_move:
                print("Tie!")
                player_points = player_points + 1
                comp_points = comp_points + 1
                print(f'Computer: {comp_points},Human: {player_points}')

            elif player_move == "Rock":
                if comp_move == "Paper":
                    print("You lose!", comp_move, "covers", player_move)
                    comp_points = comp_points + 1
                    print(f'Computer: {comp_points},Human: {player_points}')

                else:
                    print("You win!", player_move, "smashes", comp_move)
                    player_points = player_points + 1
                    print(f'Computer: {comp_points},Human: {player_points}')

            elif player_move == "Paper":
                if comp_move == "Scissors":
                    print("You lose!", comp_move, "cut", player_move)
                    comp_points = comp_points + 1
                    print(f'Computer: {comp_points},Human: {player_points}')
                else:
                    print("You win!", player_move, "covers", comp_move)
                    player_points = player_points + 1
                    print(f'Computer: {comp_points},Human: {player_points}')
            elif player_move == "Scissors":
                if comp_move == "Rock":
                    print("You lose...", comp_move, "smashes", player_move)
                    comp_points = comp_points + 1
                    print(f'Computer: {comp_points},Human: {player_points}')
                else:
                    print("You win!", player_move, "cut", comp_move)
                    player_points = player_points + 1
                    print(f'Computer: {comp_points},Human: {player_points}')
            else:
                print("That's not a valid play. Check your spelling!")


Game = game()
