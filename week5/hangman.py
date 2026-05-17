import random
import time


def menu():
  print('         ======================')
  print('         ==WELCOME TO HANGMAN==')
  print('         ======================')
  print('')
  user_choice=input('to start the game press: 1 || to exit press: 2')
  if user_choice == '1':
      start_game()
  elif user_choice == '2':
      print('         ======================')
      print('         =======GOOD BYE=======')
      print('         ======================')
      exit()



# מחזיר לי מילה רנדומלית
def random_word():
    word_list = ['apple', 'banana', 'egg','car','airplane',]
    return random.choice(word_list)


# מחזיר בחירה של המשתמש
def user_input():
    guess=input('enter your guess: ')
    return guess.lower()


# מחזיר תצוגה של מצב האותיות
def display_word(word,guessed_letter):
    display=''
    for letter in word:
        if letter in guessed_letter:
            display+=letter+' '
        else:
            display+='_ '
    return display

# ניהול המשחק
def start_game():
  word=random_word()
  guessed_letter=[]
  attempts=5

  print('      starting the game....')
  time.sleep(1)


  while attempts > 0:
      # הצגת מצב נוכחי
      current_display=display_word(word,guessed_letter)
      print(f'word: {current_display}')
      print(f'attempts: {attempts}')
      print(f'guessed_letter: {','.join(guessed_letter)}')

# בחירת המשתמש
      guess=user_input()
      if len(guess) != 1 or not guess.isalpha():
          print('please enter one letter only')
          continue


      print('cheking your guess...')
      time.sleep(1)


# בדיקה האם האות נוחשה
      if guess in guessed_letter:
          print('you already guessed this letter')
          continue

      guessed_letter.append(guess)

# בדיקה האם קיים האות במילה
      if guess in word:
          print(f'     good job there are" {guess} "in the word')
      else:
          print(f'     oh no! there are not a" {guess} "in the word')
          attempts-=1

# בדיקת ניצחון
      current_display=display_word(word,guessed_letter)
      if '_' not in current_display:
          print(f'=====YOU WIN!!! the word is {word}====')
          break

      else:
          continue
  if attempts ==0:

    print(f' game over!!! the word is {word}')
    time.sleep(1)
    print()



  menu()

menu()


