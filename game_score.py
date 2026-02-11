# game_score.py
# Demonstrates user input, type conversion, arithmetic operations, and formatted output

# Input Collection
player_name = input("Enter player name: ")

# Numeric Input Processing (convert to integer)
games_played = int(input("Enter number of games played: "))

# Score Data Entry (convert to integer)
total_score = int(input("Enter total score: "))

# Computation
if games_played > 0:
    average_score = total_score / games_played
else:
    average_score = 0

# Output Display (Formatted)
print("\nPlayer:", player_name)
print("Games Played:", games_played)
print("Total Score:", total_score)
print("Average Score:", round(average_score, 2))
