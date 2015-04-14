__author__ = 'patrickh'
# display a a menu with 3 options: write data to a file, write to a screen, and quit
ans = True
while ans:
    print (
    """
    1. write input to a file
    2. write input to the screen
    3. exit/quit
    """)
    ans = raw_input("What would you like to do?")
    # if the user chooses 1, prompt to enter another piece of data, which will write to a file
    if ans == "1":
        with open('text.txt', 'w+') as f:
            response = raw_input("Type what you feel: ")
            f.write(response)
    # if the user chooses 2, prompt to enter another piece of data, which will write to the screen
    elif ans == "2":
        response = raw_input("Type whatever you want to right now: ")
        print response
    # if the user chooses 3, quit the program
    elif ans == "3":
        print("Thanks. GOODBYE!")
        quit()

    else:
        print("Not a valid choice. Try again, bud.")