import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Try again.")

def decide_winner(user, computer):
    if user == computer:
        return 'draw'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 5

    print("\n🎮 Welcome to Rock, Paper, Scissors! 🎮")
    print(f"First to win {rounds} rounds wins the match!\n")

    for round_num in range(1, rounds + 1):
        print(f"--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == 'user':
            print("✅ You win this round!")
            user_score += 1
        elif result == 'computer':
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a draw!")

        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

    print("🎉 Game Over 🎉")
    if user_score > computer_score:
        print("🏆 Congratulations! You won the match!")
    elif computer_score > user_score:
        print("💻 Computer wins the match. Better luck next time!")
    else:
        print("😐 It's a tie overall!")

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing! 👋")
            break

main()
