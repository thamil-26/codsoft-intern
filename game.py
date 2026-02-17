import random
options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
feedback_list = []
print("=== ROCK PAPER SCISSORS GAME ===")
def winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"
while True:
    user = input("\nChoose rock / paper / scissors (or exit): ").lower()
    if user == "exit":
        break
    if user not in options:
        print("Invalid choice!")
        continue
    computer = random.choice(options)
    print("You:", user)
    print("Computer:", computer)
    result = winner(user, computer)
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    print(f"Score → You: {user_score} | Computer: {computer_score}")
print("\n=== FEEDBACK ===")
rating = input("Rate this game (1-5): ")
comment = input("Your feedback: ")
feedback_list.append((rating, comment))
print("\nThank you for your feedback!")
print("Saved Feedback:", feedback_list)
