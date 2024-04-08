import random
import tkinter as tk

words = ["GEEKS", "GIT", "DOCKER", "DEVELOPER", "RUST", "GITHUB", "WISH", "HELLO", "SOFTWARE", "PYTHON", "BASH"]
word = random.choice(words)
guessed = ['_' if letter.isalpha() else letter for letter in word]
lives = 6

hangman_parts = [
    '__',
    '|',
    'O',
    '/|\\',
    '|',
    '/\\'
    # '__\n',
    # '|\n',
    # 'O\n',
    # '/|\\\n',
    # '|\n',
    # '/\\'

]

def guess(letter):
    global lives
    if lives > 0 and '_' in guessed:
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
        else:
            lives -= 1
        update_game()

def update_game():
    guessed_label.config(text=' '.join(guessed))
    lives_label.config(text='Lives: ' + str(lives))
    hangman_label.config(text='\n'.join(hangman_parts[:6 - lives]))
    if lives <= 0:
        guessed_label.config(text='You lost! The word was: ' + word, bg = "Medium Purple", fg = "Pale Goldenrod", font="Calibri")
    elif '_' not in guessed:
        guessed_label.config(text='You won! The word was: ' + word, bg = "Medium Purple",fg = "Pale Goldenrod", font="Calibri")

# Create main window
root = tk.Tk()
root.title('Hangman')



# Add labels and buttons
guessed_label = tk.Label(root, text=' '.join(guessed), font=('Helvetica', 24))
guessed_label.pack()

lives_label = tk.Label(root, text='Lives: ' + str(lives), bg = "Indian Red", fg = "Pale Goldenrod", font=('Helvetica', 24))
lives_label.pack()

hangman_label = tk.Label(root, text='',fg = "Midnight Blue", font=('Helvetica', 24))
hangman_label.pack()

# canvas = tk.Canvas(root, width=300, height=100, bg='white')
# canvas.pack()



for ascii_value in range(65, 91):  # ASCII values for uppercase letters
    button = tk.Button(root, text=chr(ascii_value), bg = "Pale Goldenrod", command=lambda ascii_value = ascii_value: guess(chr(ascii_value)))
    button.pack(side='left')

# Start game
update_game()
root.mainloop()
