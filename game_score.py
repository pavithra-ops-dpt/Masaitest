# Input collection
name = str(input("Enter player name: "))

games_played = int(input("Enter number of games played: "))
total_score = int(input("Enter total score: "))

# Computation
average_score = total_score / games_played

# Output display (exact format)
print(f"Player: {name}")
print(f"Games Played: {games_played}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
