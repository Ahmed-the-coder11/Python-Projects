import random
MOVES = 6


saif_score = 0
ahmed_score = 0
print(f"Total Rounds are: {MOVES}")
for i in range(MOVES):

    input(f"\nPress Enter to play round {i+1}...")

    print(f"#{i+1}")
    saif_no = random.randint(1, 6)
    ahmed_no = random.randint(1, 6)
    print(f"Saif's no is: {saif_no}")
    print(f"Ahmed's no is: {ahmed_no}")
  
    saif_score += saif_no
    ahmed_score += ahmed_no

    print(f"\nSaif's score is: {saif_score}")
    print(f"Ahmed's score is: {ahmed_score}")

print("------------------------------------")

if saif_score == ahmed_score:
  print("This game's winner is NOONE!!!!!")
elif saif_score > ahmed_score:
  print("The winner of this game is SAIFFFFFFF!!!!!!!")
else:
  print("The winner of this game is AHMEDDDDD!!!!!!!!")
