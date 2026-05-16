# Input pocket money for two friends
friend1_money = int(input("Enter pocket money of Friend 1: "))
friend2_money = int(input("Enter pocket money of Friend 2: "))

if friend1_money > friend2_money:
    print("Friend 1 has more pocket money.")
elif friend2_money > friend1_money:
    print("Friend 2 has more pocket money.")
else:
    print("Both friends have the same amount of pocket money.")
