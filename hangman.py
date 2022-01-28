import random
from hangman_art import logo, stages

def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)

def print_display(string):
  print(f"{' '.join(string)}")

print(logo)

#generate number word from wordlist.txt
chosen_word = random.choice(open("wordlist.txt", "r").readline().split())

#set the variables that we will use
length_of_word = len(chosen_word)
lives = 6
end_game = False

#create a list with same length of our word and fill it with "_" 
display = []
for i in range(0,length_of_word):
  display += "_"
print_display(display)


while not end_game:
  #take a guess from the player
  guess = input("Guess a letter: \n").lower()

  clear()
  if guess in display:
    print(f"You've already guessed {guess}")

  #replace "_" with correct guesses 
  for position in range(length_of_word):
    if guess == chosen_word[position]:
      display[position] = guess

  if guess in chosen_word:
    print_display(display)
    print(stages[lives])
  else:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print_display(display)
    print(stages[lives-1])
    lives -= 1
  
  if "_" not in display:
    end_game = True
    print("You win")
  elif lives == 0:
    end_game = True
    print(f"The correct word was {chosen_word}. Game Over")
