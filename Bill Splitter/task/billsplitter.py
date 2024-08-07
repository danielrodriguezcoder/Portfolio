
#  GNU General Public License V3
#
#  Copyright (c) 2024. Daniel Rodriguez-Demers, <https://github.com/danielrodriguezcoder>

# Short script to split a bill between friends with the option to pick a lucky friend that has
# his share covered by the others.
import random

# Variables
flag_lucky = ""
dic_friends_share = {}
nb_friends = 0
split = 0.00
new_split = 0.00
lucky_friend = ""

# Main logic
try:
    nb_friends = int(input("Enter the number of friends joining (including you):"))
    if nb_friends < 1:
        print("No one is joining for the party")
    elif nb_friends == 1:
        print("No need to split, you are alone!")
    else:

        # Manages the main logic to split the cost of an activity
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(nb_friends):
            dic_friends_share[input()] = 0

        total_value = float(input("Enter the total bill value:"))
        split = round(total_value / nb_friends, 2)

        for friend in dic_friends_share:
            dic_friends_share[friend] = split

        # Logic to pick a friend that will be lucky and doesn't have to pay for the activity.
        # His share is redistributed.
        print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
        flag_lucky = input()

        if flag_lucky == "Yes":
            lucky_friend = random.choice(list(dic_friends_share))
            print(f"{lucky_friend} is the lucky one!")
            new_split = round(total_value / (nb_friends - 1), 2)
            for friend in dic_friends_share:
                if friend == lucky_friend:
                    dic_friends_share[friend] = 0
                else:
                    dic_friends_share[friend] = new_split
            print(dic_friends_share)
        else:
            print("No one is going to be lucky")
            print(dic_friends_share)

except ValueError:
    print("No one is joining for the party")
