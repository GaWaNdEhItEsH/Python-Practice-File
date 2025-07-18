# print("Hello World")
# print("Lets play a game")
# print("You have only 10 attempted to guessing a number")
# n = 18
#
# #print("Enter a number")
# i=0
# while (True):
#     print("Please guess a number")
#     num = int(input())
#     if num == 18:
#         print("Hey,You Won the Game")
#         print("you find the number in",i+1 ,"guess")
#         print("You want to play more type y for yes and n for no")
#         prt = input()
#         if prt == "y":
#             i = 0
#             continue
#         else:
#             break
#     elif num > 18 :
#         print("you enter a Greater number")
#         print("you number of guesses left",9-i)
#         if i==9:
#             print("Game over")
#             print("You want to play more type y for yes and n for no")
#             prt = input()
#             if prt == "y":
#                 i=0
#                 continue
#             else:
#                 break
#         i=i+1
#         continue
#     elif num < 18 :
#         print("you enter a leasser number")
#         print("you number of guesses left", 9-i)
#         if i==9:
#             print("Game over")
#             print("You want to play more type y for yes and n for no")
#             prt = input()
#             if prt == "y":
#                 i=0
#                 continue
#             else:
#                 break
#         i=i+1
#         continue
#     else:
#         print()



n=18

number_of_guesses = 1

def loop(number_of_guesses):
    while(number_of_guesses<=10):
        print("Number of guesses is limited to only 10 times: ")
        guess_number = int(input("Guess the number : \n"))
        if guess_number<18:
            print("You enter less number please input greater number. \n")
        elif guess_number>18:
            print("You enter greater number please enter smaller number. \n")
        else:
            print("you won\n")
            print(number_of_guesses,"no. of guesses be took to finish.")
            print("you want to play more")
            part = input("Please type y for yes & n for no\n")
            if part == "y":
                number_of_guesses = 1
                continue
            else:
                break
        print(10-number_of_guesses,"no of gausses left")
        number_of_guesses = number_of_guesses + 1
    if(number_of_guesses>10):
        print("Game Over")
        print("you want to play more")
        part = input("Please type y for yes & n for no\n")
        if part == "y":
            number_of_guesses = 1
            loop(number_of_guesses)
        else:
            exit()
loop(number_of_guesses)
