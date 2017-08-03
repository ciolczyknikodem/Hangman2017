import os
import time
import random
import datetime
import csv


capitals_list = []
tries = 0
guessed = []
costume_state = 0
lifes = 6
dash_capital = []


def load_countries_and_capitals():
    """ Argument: None
        Return: None

        Function load countries and capitals from file"""

    global capitals_list
    for line in open("countries_and_capitals", 'r').readlines():
        temp = []
        temp.append(line.split(" | ")[0].upper())
        temp.append(line.split(" | ")[1].replace('\n', "").upper())
        capitals_list.append(temp)


def draw_menu_scene():
    """ Argument: None
        Return: None

        Function draws main menu when the player run the program or return after failed/finished game"""

    bad_answer = False
    costume_state = 0
    scene = open("MainMenuScene", 'r').readlines()
    global x
    x = True

    while(x):
        os.system('clear')

        for line in scene:
            print(line, end='')

        choice = None

        if bad_answer is not True:
            choice = input("Your Choice: ")

        if bad_answer is True:
            choice = input("Bad Choice, Try Again: ")

        if choice == "1":
            x = False
            stage()

        elif choice == "2":
            x = False
            os.system('clear')
            score = open_lader_board()
            score_board = calculate_position(score)
            draw_leaderboard_scene(score_board)
            input('\nEneter any key to back')
            draw_menu_scene()

        elif choice == "3":
            draw_help_scene()
            x = False

        elif choice == "4":
            draw_quit_scene()
            exit()

        else:
            bad_answer = True
            continue


def draw_quit_scene():
    """ Argument: None
        Return: None

        Function draws a quit scene, when player decided to leave the game."""

    os.system('clear')
    scene = open("GameQuitScene", 'r').readlines()

    for line in scene:
        print (line, end='')


def pick_random_capital(capitals_list):
    """ Argument: List of strings
        Return: List of string

        Function take all capitals with countries, chose 1 of them
        and return 1 randomly position of all capitals/countries """

    GuessingCapitalCountry = random.choice(capitals_list)
    return GuessingCapitalCountry


def change_capital_to_dash(guessing_capital):
    """ Argument: List of strings
        Return: List of dash

        Function take capital as string, make new list, with same number of dashes like guessing capital have"""

    guessing_capital = guessing_capital[1]
    dash_capital = []

    for letter in guessing_capital:

        if letter == " ":
            dash_capital.append(" ")

        elif not letter.isdigit():
            dash_capital.append("_")
    globals().__setitem__("dash_capital", dash_capital)


def draw_help_scene():
    """ Argument: None
        Return: None

        Function draws help scene, when player need help, by pressing 3 in the main menu"""
    os.system('clear')
    lines = open("HelpScene", 'r').readlines()

    for line in lines:
        print(line, end='')

    print("")
    input("Press ENTER to back to main menu. ")
    draw_menu_scene()


def stage():
    """ Argument: None
        Return: None

        Function starts game, when the player pressed 1 in main menu or decided to play again"""
    global dash_capital, lifes, costume_state, tries, guessed
    lifes = 6
    tries = 0
    costume_state = 0
    guessed = []
    globals().__setitem__("guessingTime", time.time())
    GuessingCapitalCountry = pick_random_capital(capitals_list)
    change_capital_to_dash(GuessingCapitalCountry)

    while True:
        os.system('clear')

        for line in open("MainGameScene", 'r').readlines():

            if line.__contains__("%COSTUME"):
                draws_a_costume()
                continue

            if line.__contains__("%LIFES") and line.__contains__("%TIME"):

                ActualTime = time.time()
                line = line.replace("%LIFES", str(globals().get("lifes")))
                timeDifference = ActualTime - globals().get("guessingTime")
                line = line.replace("%TIME", int(timeDifference).__str__() + " seconds")

            if line.__contains__("%TRIES"):
                line = line.replace("%TRIES", tries.__str__())

            if line.__contains__("%GUESSED"):
                line = line.replace("%GUESSED", ",".join(guessed))

            if line.__contains__("%CAPITAL"):
                dash_capital = globals().get("dash_capital")
                dash_string = " ".join(dash_capital)
                line = line.replace("%CAPITAL", dash_string)

            if line.__contains__("%HINT"):
                line = line.replace("%HINT", hint(lifes, GuessingCapitalCountry))

            print (line)

        if lifes <= 0:  # Check if player lose, ask for play again or back to menu
            time.sleep(1)
            lose_stage()
            draw_leaderboard_scene()
            play_again()

        if str(dash_capital).__contains__("_") is False:  # Check if player won, save score, display leader board
            ActualTime = time.time()
            timeDifference = ActualTime - globals().get("guessingTime")
            time.sleep(1)

            score = (lifes * 2000)/tries - timeDifference
            score = str(score).split(".")[0]
            timer = round(timeDifference, 0)

            end_stage_success(score)
            os.system('clear')
            highscore(timer, tries, GuessingCapitalCountry, int(score))

            score_board = open_lader_board()
            scene = calculate_position(score_board)

            draw_leaderboard_scene(scene)
            play_again()
        check_if_asnwer_correct(GuessingCapitalCountry)


def check_if_asnwer_correct(guessing_capital):
    """ Argument: string
        Return: None

        Function checks if player typed wrong or right answer. If typed righ answer increment tries variable, otherwise decetrements lifes and increments tries variables"""
    capital = str(guessing_capital[1]).upper()
    answer = input("                                            Guess a letter or the whole word: ")
    answer = answer.upper()
    dash_capital = globals().get("dash_capital")
    global tries

    if answer.isalpha() and answer.__len__() == 1:
        contains = False
        i = 0

        for x in capital:

            if(x == answer):
                dash_capital[i] = answer
                contains = True

            i += 1

        if contains is True:
            globals().__setitem__("dash_capital", dash_capital)

        else:
            global costume_state, lifes
            costume_state += 1
            lifes -= 1

        if(guessed.__contains__(answer) is False):
            guessed.append(answer)
        tries += 1
    answer = answer.replace(" ", "")
    capital = capital.replace(" ", "")

    if(answer.isalpha() and answer.__len__() > 1):

        if(capital == answer):
            globals().__setitem__("dash_capital", answer)

        else:
            # global  costume_state,lifes
            costume_state += 1
            lifes -= 2
        if guessed.__contains__(answer) is False:
            guessed.append(answer)
        tries += 1


def draws_a_costume():
    """ Argument: None
        Return: None

        Functions draws costume why player plays the game. The type of costume depeds on lifes amount variable"""

    costumes = open("HangmanPictures", 'r').readlines()
    global costume_state
    if(costume_state == 0):

        for i in range(0, 20):
            print("")

    elif(costume_state == 6):

        for i in range(0, 10):
            print(costumes[i])

    elif(costume_state == 5):

        for i in range(9, 19):
            print(costumes[i])

    elif(costume_state == 4):

        for i in range(18, 28):
            print(costumes[i])

    elif(costume_state == 3):

        for i in range(27, 37):
            print(costumes[i])

    elif(costume_state == 2):

        for i in range(36, 46):
            print(costumes[i])

    elif(costume_state == 1):

        for i in range(45, 55):
            print(costumes[i])


def hint(lifes, country_of_guessing_capital):
    """ Argument: None
        Return: None

        Function shows a hint when player have 1 life left."""
    if lifes == 1:
        country_of_guessing_capital = str("Hint: " + country_of_guessing_capital[0])

    else:
        country_of_guessing_capital = ""

    return country_of_guessing_capital


def open_lader_board():
    """Argument: None
       Return: List

       Function read data from file and make them list"""

    leaderboard = []

    with open('Leaderboard.txt', 'r', newline='') as f:
        reader = csv.reader(f, delimiter='|', skipinitialspace=True)

        for row in reader:
            leaderboard.append(row)

    return leaderboard


def draw_leaderboard_scene(score):
    """Argument: List
       Return: None

       Function display asci Art and run drawing_highscore function"""

    with open('LeaderboardScreen.txt', 'r') as f:
        reader = f.read()

    print(reader)

    highscore = draw_highscore(score)


def draw_highscore(score):
    """Argument: List of scores
       Return: None

       Function take list of players scores and display best 10 scores"""

    for index in range(len(score)):
        pts = score[index][5]
        pts = str(pts)
        del score[index][5]
        score[index].insert(5, pts)

    max_lenght_word = 0
    position_lenght = 0

    for row in score:
        for word in row:
            if len(word) > max_lenght_word:
                max_lenght_word = len(word)

    for row in range(len(score)):

        if row < 10:
            position_lenght = row+1
            position_lenght = str(position_lenght)

            if len(position_lenght) > 1:

                position_lenght = int(position_lenght)

                print(" " * (max_lenght_word - 1) + str(position_lenght) + ". " + score[row][0] + " " *
                      (max_lenght_word - len(score[row][0])) + "|" + " "*5 + score[row][5] + " pts")

            else:

                position_lenght = int(position_lenght)

                print(" " * max_lenght_word + str(position_lenght) + ". " + score[row][0] +
                      " " * (max_lenght_word - len(score[row][0])) + "|" + " "*5 + score[row][5] + " pts")
        else:
            break


def highscore(time, tries, guessing_word, score):
    """Argument: strings
       Return: List of strings

       Function make list of info about plers game"""

    name = input("Enter your nick:\n")

    highscore = []
    current_date = datetime.date.today()
    guessing_word = "".join(guessing_word[1])

    highscore.append(name)
    highscore.append(current_date)
    highscore.append(time)
    highscore.append(tries)
    highscore.append(guessing_word)
    highscore.append(score)

    save_highscore(highscore)
    os.system('clear')

    return highscore


def save_highscore(scores):
    """ Argument: List
        Return: None"""

    with open('Leaderboard.txt', 'a', newline='') as f:
        w = csv.writer(f, delimiter='|')
        w.writerow(scores)


def calculate_position(leaderboard):
    """ Argument: List
        Return: List

        Function use bubble sort to sorting list of players scores"""

    scores = []

    for index in range(len(leaderboard)):
        scores.append([leaderboard[index][0], leaderboard[index][1], leaderboard[index][2], leaderboard[index][3],
                      leaderboard[index][4], int(leaderboard[index][5])])

    start = True

    while start:

        start = False

        for index in range(len(scores)-1):

            if scores[index][5] < scores[index+1][5]:

                scores[index][5], scores[index+1][5] = scores[index+1][5], scores[index][5]
                start = True

    return scores


def end_stage_success(score):
    """ Argument: List
        Return: None

        Function prints end stage if player won the game"""

    os.system('clear')

    for line in open("SuccessScene", 'r').readlines():

        if(line.__contains__("%SCORE")):
            line = line.replace("%SCORE", str(score).split(".")[0])

        print(line, end='')
    time.sleep(3)


def play_again():
    """Argument: None
       Return: None

       Function ask player to play again or back to menu"""

    answer = input("\nType any key to try again or '!' to get main menu. ")

    if(answer == "!"):
        draw_menu_scene()

    else:
        stage()


def lose_stage():
    """ Argument: None
        Return: None

        Function prints end stage if player won the game"""
    os.system('clear')
    for line in open("LoseStageScene", 'r').readlines():
        print(line, end='')
    answer = input("Type any key to try again or '!' to get main menu. ")
    if(answer == "!"):
        draw_menu_scene()
    else:
        stage()


def main():
    load_countries_and_capitals()
    draw_menu_scene()


if __name__ == '__main__':
    main()
