import os
import time
import random
import datetime
import operator
import csv

capitals_list = []
tries = 0
guessed = []
costume_state = 0
lifes = 6
dash_capital = []


def load_countries_and_capitals():

    global capitals_list

    for line in open("countries_and_capitals", 'r').readlines():
        temp = []
        temp.append(line.split(" | ")[0].upper())
        temp.append(line.split(" | ")[1].replace('\n', "").upper())
        capitals_list.append(temp)


def draw_menu_scene():

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
            draw_leaderboard_scene(score)

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
    print(GuessingCapitalCountry)
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
    os.system('clear')
    lines = open("HelpScene", 'r').readlines()
    for line in lines:
        print(line, end='')
    print("")
    input("Press ENTER to back to main menu. ")
    draw_menu_scene()


def stage():
    global dash_capital
    globals().__setitem__("guessingTime", time.time())
    GuessingCapitalCountry = pick_random_capital(capitals_list)
    change_capital_to_dash(GuessingCapitalCountry)
    global lifes, costume_state
    lifes = 6
    costume_state = 0
    while(True):
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

        if(lifes <= 0): # sprawdza czy uzytkownik przegrał
            print("You have run out of your lives!")
            end = time.time()
            time.sleep(1)
            exit()

        if(str(dash_capital).__contains__("_") == False): #sprawdza czy użytkownik wygrał
            print("You won")
            time.sleep(1)
            end = time.time()
            score_time = round(end - ActualTime, 2)
            leaderboard = open_lader_board()
            highscore(lifes, score_time, tries, GuessingCapitalCountry, leaderboard)
        check_if_asnwer_correct(GuessingCapitalCountry)


def check_if_asnwer_correct(guessing_capital):
    # Funkcja pobiera informacje o lieterze/slowie uzytkowinika i podmienia _ w zgadywanym miescie na litery, argument zgadywana stolica, return liste stringow
    capital = str(guessing_capital[1]).upper()
    answer = input("                                            Guess letter or the whole word (type ! to exit): ")
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
            i+=1
        if(contains == True):
            globals().__setitem__("dash_capital", dash_capital)
        else:
            global  costume_state,lifes
            costume_state +=1
            lifes -=1
        if(guessed.__contains__(answer) == False):
            guessed.append(answer)
        tries += 1
    answer = answer.replace(" ", "")
    capital = capital.replace(" ", "")
    if(answer.isalpha() and answer.__len__() > 1):
        if(capital == answer):
            globals().__setitem__("dash_capital", answer)
        else:
            # global  costume_state,lifes
            costume_state +=1
            lifes -=2
        if(guessed.__contains__(answer) == False):
            guessed.append(answer)
        tries += 1


def draws_a_costume():

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

    if lifes == 1:
        country_of_guessing_capital = str("Hint: " + country_of_guessing_capital[0])

    else:
        country_of_guessing_capital = ""

    return country_of_guessing_capital


def open_lader_board():

    leaderboard = []

    with open('Leaderboard.txt', 'r', newline='') as f:
        reader = csv.reader(f, delimiter='|', skipinitialspace=True)

        for row in reader:
            leaderboard.append(row)

    score = calculate_position(leaderboard)

    return score


def draw_leaderboard_scene(score):

    with open('LeaderboardScreen.txt', 'r') as f:
        reader = f.read()

    print(reader)

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

    input('\n Enter any key to back to menu:')
    draw_menu_scene()


def highscore(lifes, time, tries, guessing_word, leaderboard):

    name = input("Enter your nick:\n")

    highscore = []
    current_date = datetime.date.today()

    lifes = lifes * 10
    tries = lifes * 2
    guessing_word = "".join(guessing_word[1])
    time = int(round(time, 0))

    score = 100 + lifes - tries - time # Score jest zle wyliczany, trzeba pogrzebac w zmiennych i zrobic sensownie to dzialanie.
                                       # Nie mozesz miec floatow bo nie bedzie sortowal
    print (score)

    highscore.append(name)
    highscore.append(current_date)
    highscore.append(time)
    highscore.append(tries)
    highscore.append(guessing_word)
    highscore.append(score)

    save_highscore(highscore)
    leaderboard = open_lader_board()
    # calculate_position(leaderboard)
    score = calculate_position(leaderboard)
    draw_leaderboard_scene(score)


def save_highscore(scores):
    """ Argument: List
        Return: None

        Function save scores to file"""

    with open('Leaderboard.txt', 'a', newline='') as f:
        w = csv.writer(f, delimiter='|')
        scores = scores[0], scores[1], scores[2], scores[3], scores[4], scores[5], "pts"
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


def main():
    load_countries_and_capitals()
    draw_menu_scene()


if __name__ == '__main__':
    main()
