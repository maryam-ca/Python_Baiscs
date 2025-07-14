import os

# File to save highest score
FILENAME = "high_score.txt"

# Load highest score from file
def load_high_score():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return int(file.read())
            except:
                return 0
    return 0

# Save highest score to file
def save_high_score(score):
    with open(FILENAME, "w") as file:
        file.write(str(score))

# Questions and answers
quiz = [
    ("What is the capital of Pakistan?", "islamabad"),
    ("How many days are there in a week?", "7"),
    ("Which planet is known as the Red Planet?", "mars"),
    ("What is 5 + 3?", "8"),
    ("Which language is used to write Python?", "english")
]

# Main game
def play_quiz():
    score = 0
    for question, correct_answer in quiz:
        print("\n" + question)
        user_answer = input("Your answer: ").lower().strip()
        if user_answer == correct_answer:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer: {correct_answer}")

    print(f"\n Your score: {score}/{len(quiz)}")

    high_score = load_high_score()
    if score > high_score:
        print(" New High Score!")
        save_high_score(score)
    else:
        print(f" Highest Score: {high_score}")

# Run the game
if __name__ == "__main__":
    print("🎮 Welcome to the Quiz Game!")
    play_quiz()
