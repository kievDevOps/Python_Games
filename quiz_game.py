#-------------------------------

def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------------------------")
        print(key) 
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (1, 2, 3 or 4): ")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)

#-------------------------------

def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    
#-------------------------------

def display_score(correct_guesses, guesses):
    
    print("--------------------------------------------")
    print("RESULTS")
    print("--------------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses? ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

#-------------------------------

def play_again():
    
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

#-------------------------------

questions = {  # dictionary with questions
    "What is Kiev's true first name?: ": "1",
    "What is Kiev's favorite coding language?: ": "2",
    "What is Kiev's favorite food?: ": "3",
    "What is Kiev's favorite country?: ": "1"
    }

options = [["1. Felippe", "2. Carlos", "3. Nathan", "4. Michael"],
           ["1. Php", "2. Python", "3. JavaScript", "4. C#"],
           ["1. Strogonoff", "2. Pizza", "3. Yakisoba", "4. Burrito"],
           ["1. Switzerland", "2. Japan", "3. Germany", "4. Canada"]]  # 2d lists with options for each question

new_game()

while play_again():
    new_game()

print("Bye! Thank you for playing!")
