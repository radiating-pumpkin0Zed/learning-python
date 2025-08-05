import random
words = ["witty", "grind", "title", "apart", "flame", "spite", "shine"]

answer = random.choice(words)

for attempt in range (6):
    guess = input(f"Attempt {attempt + 1}/6: ").lower()

    if len(guess) != 5 or guess not in words:
        print("❌ Invalid guess. Try a 5-letter word from the list.")
        continue

    result = ""
    for i in range(5):
        if guess[i] == answer[i]:
            result += "🟩"
        elif guess[i] in answer:
            result += "🟨"
        else:
            result += "⬛"
    print(result)

    if guess == answer:
        print("🎉 Congratulations! You've guessed the word!")
        break
    else:
        print(f"💀 Out of tries! The word was: {answer}")
