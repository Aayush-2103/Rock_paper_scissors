#Rock paper scissor
from random import randint
while True:
    options = ['rock', 'paper', 'scissor']
    print('\t\t*****RULE BOOK*****\n')
    print("1) Input is case sensitive so be careful while entering your option")
    print("2) If by chance you make a mistake while input then your 1 chance is lost that can't be retrived")
    print('3) All the best play carefully!\n\n')

    name=input('Enter your name user:- ')
    print('Good luck!', name)
    print('ROCK PAPER SCISSOR\n\n')

    p_pc,p_user=0,0
    t=10

    for i in range(t):
        pc=options[randint(0,len(options)-1)]
        user=input('Enter one out of rock, paper, or scissor:- \nYour choice is-- ')
        if user == 'rock':
            if pc == 'rock':
                print('PC- ', pc)
                print('\nScore')
                print('User- ',p_user)
                print('PC- ', p_pc)
                continue
            elif pc == 'paper':
                p_pc+=1
                print('PC- ', pc)
                print('\nScore')
                print('User- ',p_user)
                print('PC- ', p_pc)
            elif pc == 'scissor':
                p_user+=1
                print('PC- ', pc)
                print('\nScore')
                print('User- ',p_user)
                print('PC- ', p_pc)

        elif user == 'paper':
            if pc == 'rock':
                p_user+=1
                print('PC- ', pc)
                print('\nScore')
                print('User- ',p_user)
                print('PC- ', p_pc)
            elif pc == 'paper':
                print('PC- ', pc)
                print('\nScore')
                print('User- ',p_user)
                print('PC- ', p_pc)
                continue
            elif pc == 'scissor':
                p_pc+=1
                print('PC- ', pc)
                print('\nScore')
                print('User- ',p_user)
                print('PC- ', p_pc)

        elif user == 'scissor':
            if pc == 'rock':
                p_pc+=1
                print('PC- ', pc)
                print('\nScore')
                print('User- ',p_user)
                print('PC- ', p_pc)
            elif pc == 'paper':
                p_user+=1
                print('PC- ', pc)
                print('\nScore')
                print('User- ',p_user)
                print('PC- ', p_pc)
            elif pc == 'scissor':
                print('PC- ', pc)
                print('\nScore')
                print('User- ',p_user)
                print('PC- ', p_pc)
                continue

        else:
            print('\t\t*****Enter one out of rock, paper, or scissor only.')

    print('\n\n', name, 'your score is- ', p_user)
    print("\nComputer's score is:- ", p_pc,'\n\n')

    #who won
    if p_user > p_pc:
        print('Hurray!', name, 'you won')
    elif p_pc > p_user:
        print('Bad Luck!', name, 'you lost')
    else:
        print('DRAW')

    print('\n\n')
    if input('Do you want have the courage to play again ?(y/n):- ') == 'n':
        break