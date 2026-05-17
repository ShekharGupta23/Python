# Taking input for scores of three players
player1_score = int(input("Enter the score of Player 1: "))
player2_score = int(input("Enter the score of Player 2: "))
player3_score = int(input("Enter the score of Player 3: "))

if player1_score > player2_score and player1_score > player3_score:
    print("Player 1 scored the highest with", player1_score, "runs.")
elif player2_score > player1_score and player2_score > player3_score:
    print("Player 2 scored the highest with", player2_score, "runs.")
elif player3_score > player1_score and player3_score > player2_score:
    print("Player 3 scored the highest with", player3_score, "runs.")
else:
    print("It's a tie between players!")
