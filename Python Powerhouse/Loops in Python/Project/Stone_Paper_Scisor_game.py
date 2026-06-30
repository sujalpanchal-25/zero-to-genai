# import random

# choices = ["stone", "paper", "scissor"]
# pc_c = 0
# user_c = 0

# print("Welcome to Stone, Paper, Scissor!\n")
# print("Type 'q' to stop playing.")

# while True:
#     user_choice = input("\nEnter your choice (stone/paper/scissor): ").lower()
    
#     if user_choice == 'q':
#         print("Thanks for playing!\n")
#         break
        
#     if user_choice not in choices:
#         print("Invalid choice, please try again.")
#         continue
#     random.shuffle(choices)   
#     computer_choice = random.choice(choices)
#     print(f"Computer chose: {computer_choice}")
    
#     if user_choice == computer_choice:
#         print("It's a tie!\n")
#         pc_c += 1
#         user_c += 1
#     elif user_choice == "stone" and computer_choice == "scissor":
#         print("You win!\n")
#         user_c += 1
#     elif user_choice == "paper" and computer_choice == "stone":
#         print("You win!\n")
#         user_c += 1
#     elif user_choice == "scissor" and computer_choice == "paper":
#         print("You win!\n")
#         user_c += 1
#     else:
#         print("Computer wins!\n")
#         pc_c += 1

# print(f"Computer Score : {pc_c}")
# print(f"User Score {user_c}")

import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

choices = ["stone", "paper", "scissor"]

user_score = 0
computer_score = 0
round_no = 1

print(Fore.CYAN + "=" * 50)
print(Fore.YELLOW + "🎮 STONE PAPER SCISSOR - FUTURE EDITION 🎮")
print(Fore.CYAN + "=" * 50)
print("Type 'q' anytime to quit.\n")

while True:

    print(Fore.MAGENTA + f"\n========== ROUND {round_no} ==========")

    user_choice = input(
        Fore.GREEN +
        "👉 Enter your choice (stone/paper/scissor): "
    ).lower()

    if user_choice == "q":
        break

    if user_choice not in choices:
        print(Fore.RED + "❌ Invalid Choice!")
        continue

    print(Fore.YELLOW + "\n🤖 Computer is thinking", end="")

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    computer_choice = random.choice(choices)

    emoji = {
        "stone": "🪨",
        "paper": "📄",
        "scissor": "✂️"
    }

    print("\n")
    print(f"👤 You      : {emoji[user_choice]} {user_choice}")
    print(f"🤖 Computer : {emoji[computer_choice]} {computer_choice}")

    # Result Logic
    if user_choice == computer_choice:
        print(Fore.CYAN + "\n🤝 It's a Tie!")
    elif (
        (user_choice == "stone" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "stone") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        print(Fore.GREEN + "\n🏆 You Win This Round!")
        user_score += 1
    else:
        print(Fore.RED + "\n💀 Computer Wins This Round!")
        computer_score += 1

    print(Fore.BLUE + "\n📊 LIVE SCOREBOARD")
    print(Fore.BLUE + "-" * 25)
    print(f"👤 You      : {user_score}")
    print(f"🤖 Computer : {computer_score}")

    round_no += 1

# Final Result
print("\n")
print(Fore.CYAN + "=" * 50)
print(Fore.YELLOW + "🏁 MATCH OVER 🏁")
print(Fore.CYAN + "=" * 50)

print(f"👤 Final User Score      : {user_score}")
print(f"🤖 Final Computer Score  : {computer_score}")

if user_score > computer_score:
    print(Fore.GREEN + "\n🎉 CONGRATULATIONS! YOU WON THE MATCH!")
elif computer_score > user_score:
    print(Fore.RED + "\n💀 COMPUTER WON THE MATCH!")
else:
    print(Fore.CYAN + "\n🤝 MATCH DRAW!")

print(Fore.YELLOW + "\nThanks For Playing ❤️")