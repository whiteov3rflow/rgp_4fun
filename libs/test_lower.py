import random
attacks = {"Basic":10,"Powerfull":50,"Fatal":100}
points = 100

choice = random.choice(list(attacks.keys()))
print(list(attacks.keys()))

# if choice in attacks:
#     retrieve_points = attacks[choice]
#     points -= retrieve_points
#     print(f'{choice} attaque: tu perds {retrieve_points} points')

# def get_use_input() -> str:
#     text = input("Type your choice: ")
#     if text.lower() == 'y' or "yes":
#         print("Nice use of lower() function")
#         print(text.lower())
# get_use_input()

SECRET = "insec{34sy_7h3_g4m3_w4s_1337}"
count = len(SECRET)
for chr in SECRET:
    count += 1
    print(f"You won the game is your reward {chr[0]}")