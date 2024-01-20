import random

def diff_test(): #This part of code will test difficulty of the game for the 2 different modes
    while True:
     try:
      diff = int(input("Type 1 for difficulty kid(10 chances and hints), 2 for difficulty normal(5 chances and hints), 3 for difficulty sigma(3 chances and no hints) and 4 for difficulty gigachad(1 chance and no hints):"))
      if diff > 4 or diff < 1:
        raise
      else:
          break
     except:
        print("Type a valid game difficulty")
        continue
    return diff

def user_guess(): #This is the code for the user guess mode
    print("Ok, now you will guess the number!\n\n")
    diff = diff_test()
    user_starting_num = int(input("The starting number of the range:"))
    user_ending_num = int(input("The ending number of the range:")) + 1
    num_lis = tuple(range(user_starting_num,user_ending_num))
    num = random.choice(num_lis)

    if diff == 1:
        chances = 10
        hints = 10
    elif diff == 2:
        chances = 5
        hints = 5
    elif diff == 3:
        chances = 3
        hints = 0
    else:
        chances = 1
        hints = 0

    while chances > 0:
        guess = int(input("Your guess:"))
        if guess == num:
            return True, num
        else:
            chances-=1
            if chances > 0 and not(chances < 0):
                print("Try again")
                if hints > 0:
                    if num > guess:
                        print("Your guess was lesser than the number.")
                    elif num < guess:
                        print("Your guess was greater than the number.")
            else:
                return False, num

def python_guess(): #This is the code for computer guess mode
    print("Ok, now I will guess the number!\n\n")
    diff = diff_test()
    if diff> 4:
        raise
    if diff == 1:
        chances = 10
        hints = 10
    elif diff == 2:
        chances = 5
        hints = 5
    elif diff == 3:
        chances = 3
        hints = 0
    else:
        chances = 1
        hints = 0
    loop = 1
    guess_tuple = []  
    while chances > 0:
        if loop == 1:
            user_starting_num = int(input("The starting number of the range:"))
            user_ending_num = int(input("The ending number of the range:")) + 1
            num_lis = tuple(range(user_starting_num,user_ending_num))
            num = random.choice(num_lis)
            guess_lis = [num]
            guess_tuple.append(num)

        print(f"My guess: {num}")
        ans = input("Type 'same' if my guess was correct or press enter if it was incorrect:")

        if ans == 'same':
            return False
        else:
            loop+=1
            chances-=1
            if chances > 0 and not(chances < 0):
                if hints > 0:
                    hint = input("Type '>' if my guess was greater than the number or '<' if my guess was the lesser:")
                    if hint == '>':
                        user_ending_num = num 
                    elif hint == '<':
                        user_starting_num = num + 1
                    num_lis = tuple(range(user_starting_num,user_ending_num))
                    num = random.choice(num_lis)
                    guess_tuple.append(num)
                else:
                    num = random.choice(num_lis)
                    while True:
                     if num in guess_lis:
                        num = random.choice(num_lis)
                     else:
                        guess_lis.append(num)
                        guess_tuple.append(num)
                        break
            else:
                return True, tuple(guess_tuple) 
            
print("Welcome,\n        to the game of guesses:-")

while True: #This is the main code where all the code is used to output answers
    try:
        game = input("If you want to guess type'ME' or type 'YOU' for me to guess:")
        if game == 'ME':
            start = 1
        elif game == 'YOU':
            start = 0
        else:
            raise

    except:
        print("Type a correct game:")
        continue
    else:
        print("Let's start Playing")

    if start == 1:
        win, num = user_guess()
        if win == True:
            print(f"You won! The number was {num}")
        else:
            print(f"You lost, the correct number was{num}")
    else:
        win, num = python_guess()
        if win == True:
            print(f"You won well what was the correct num?")
            ver = int(input("Number?:"))
            if ver in num:
                print("You cheater!")
        else:
            print(f"I won!")

    if 'exit' in input("Type 'exit' to leave or press enter to play again:"):
        print("Bye!\n",end="     ")
        print("By, Sargun Singh")
        input("Confirm Leave!")
        break