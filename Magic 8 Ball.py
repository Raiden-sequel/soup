import random

name = input('what is your name? : ')
print('welcome to my office, ' + name)
print(' ')
while True:
    
    question = input('what do you wish to know? : ')
    answer_num = random.randint(1, 5)

    if answer_num == 1:
        print('the answer is yes')

    if answer_num == 2:
        print('the answer is no')

    if answer_num == 3:
        print('perhaps')

    if answer_num == 4:
        print('I have no clue')

    if answer_num == 5:
        print('I dont want to tell you :)')
        
    print(' ')
