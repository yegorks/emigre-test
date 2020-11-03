secret_password = "zebra"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

nickname = input("Enter hacker's nickname: ")
password = input("Enter hacker's password and be careful if there is NO input: ")

if password != "NO":
    print(nickname + ", why did you write your password? ")
elif password == "NO":
    print(nickname + ", you are smart!\n" +
    "Can you help to crack the password?\n" +
    "To answer this question you should print y or n:")
    answer = input()

    while answer != "y" and answer != "n":
        answer = input("Incorrect answer (you should input only y or n)")
    if answer == "y":
        print(nickname + ", you made the right decision! ")
        print(nickname + ", that password is an ANIMAL. You have only " + str(guess_limit) + " attempts.\n" +
        "Let's try to guess!")
        while guess != secret_password and not (out_of_guesses):
            if guess_count < guess_limit:
                guess = input("Enter guess: ")
                guess_count += 1
            else:
                out_of_guesses = True
        if out_of_guesses:
            print(nickname + ", unfortunately, you LOSE!")
        else:
            print(nickname + ", you WON! You got the secret word!")
    elif answer == "n":
        print(nickname + ", well, okay... will find another")



