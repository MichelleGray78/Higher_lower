import art
from game_data import data
import random

data_sample = random.sample(data, 2)
score = 0

# Checking if data is the same and if it is - choosing another random item
if data_sample[0] == data_sample[1]:
    data_sample[1] = random.choice(data)

def set_up(data_sample, score):
    print(art.logo)
   
    # Getting first comparison choice from the list
    data_A_name = data_sample[0]["name"]
    data_A_description = data_sample[0]["description"]
    data_A_country = data_sample[0]["country"]

    print(f"Compare A: {data_A_name}, {data_A_description}, from {data_A_country}.")

    # Getting second comparision choice from the list
    data_B_name = data_sample[1]["name"]
    data_B_description = data_sample[1]["description"]
    data_B_country = data_sample[1]["country"]
    print(art.vs)
    print(f"Against B: {data_B_name}, {data_B_description}, from {data_B_country}.")
    
    compare(data_sample, score)

def compare(data_sample, score):
    end_game = False
    while end_game != True:
        who_has_more = input("Who has more Instagram followers? Type 'A' or 'B' ").upper()
        if who_has_more == "A":
            if data_sample[0]["follower_count"] > data_sample[1]["follower_count"]:
                score += 1
                print(f"Right answer, score = {score}")
                data_sample[0] = data_sample[1]
                data_sample[1] = random.choice(data)
                set_up(data_sample, score)
            else:
                end_game = True
                print(f"Wrong answer, total score = {score}")
                quit()
        elif who_has_more == "B":
            if data_sample[1]["follower_count"] > data_sample[0]["follower_count"]:
                score += 1
                print(f"Right answer, score = {score}")
                data_sample[0] = data_sample[1]
                data_sample[1] = random.choice(data)
                set_up(data_sample, score)
            else:
                end_game = True
                print(f"Wrong answer, Total score = {score}")
                quit()
        else:
            print("Invalid input - please try again")
            compare(data_sample, score)


# Checking the player wants to play
wanna_play = input("Would you like to play higher/lower? Type 'y' for yes or 'n' for no: ").lower()
if wanna_play == "y":
    set_up(data_sample, score)
else:
    print("Goodbye!")
    quit()

