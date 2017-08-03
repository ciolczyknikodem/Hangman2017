import os
import time
import random
import datetime
import operator
import csv


capitals_list = []
tries = 0
guessed = []
costume_state = 0;
lifes = 6;
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
            draw_leaderboard_scene()

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
    lifes = 6; tries = 0 ; costume_state = 0 ; guessed = []
    globals().__setitem__("guessingTime", time.time())
    GuessingCapitalCountry = pick_random_capital(capitals_list)
    change_capital_to_dash(GuessingCapitalCountry)
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
            time.sleep(1)
            lose_stage()

        if(str(dash_capital).__contains__("_") == False): #sprawdza czy użytkownik wygrał
            ActualTime = time.time()
            timeDifference = ActualTime - globals().get("guessingTime")
            time.sleep(1)
            score = (lifes * 2000)/tries - timeDifference
            end_stage_success(score)
            # end = time.time()
            # score_time = round(end - ActualTime, 2)
            # leaderboard = open_lader_board()
            # highscore(lifes, score_time, tries, GuessingCapitalCountry, leaderboard)
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
    # Czytanie z pliku dziala elegancko
    leaderboard = []

    with open('Leaderboard.csv', 'r', newline='') as f:
        reader = csv.reader(f, delimiter='|', skipinitialspace=True)

        for row in reader:
            leaderboard.append(row)

    return leaderboard


def draw_leaderboard_scene():
    # Tutaj jak narazie dziala tylko czytanie asci art
    # Trzeba zrobic zmienna max_item_lenght i wzgledem jej dlugosci printowac liste wynikow tj. dlugosc - dlugosc wstawianej rezczy i wtedy | itd
    # Jak cos jutro to moge zrobic
    with open('LeaderboardScreen.txt', 'r') as f:
        reader = f.read()

    print(reader)

    leaderboard = open_lader_board()
    print(leaderboard)

    max_item_lenght = 0

    for item in leaderboard:

        for words in item:
            words.split()

            for letters in words:
                letters.split()

                if len(words) > max_item_lenght:
                    max_item_lenght = len(words)

    input('Enter any key to back to menu:')
    draw_menu_scene()


def highscore(lifes, time, tries, guessing_word, leaderboard):

    name = input("Enter your nick:\n")

    highscore = []
    current_date = datetime.date.today()

    lifes = lifes * 10
    tries = lifes * 2
    guessing_word = "".join(guessing_word[1])
    print(time)
    time = int(round(time, 0))
    print(time)

    score = 100 + lifes - tries - time # Score jest zle wyliczany, trzeba pogrzebac w zmiennych i zrobic sensownie to dzialanie.
                                       # Nie mozesz miec floatow bo nie bedzie sortowal
    print (score)

    highscore.append(name)
    highscore.append(current_date)
    highscore.append(time)
    highscore.append(tries)
    highscore.append(guessing_word)
    highscore.append(score)

    # leaderboard.append(highscore)
    print(highscore)
    save_highscore(highscore)
    leaderboard = open_lader_board()
    print(leaderboard)
    calculate_position(leaderboard)
    draw_leaderboard_scene()


def save_highscore(scores):
    """ Argument: List
        Return: None

        Function save scores to file"""
# Save dziala elegancko
    with open('Leaderboard.csv', 'a', newline='') as f:
        w = csv.writer(f, delimiter='|')
        scores = [scores[0], scores[1], scores[2], scores[3], scores[4], scores[5]]
        w.writerow(scores)


def calculate_position(leaderboard):
    """ Argument: List
        Return: List

        Function use bubble sort to sorting list of players scores"""

    scores = []
    # Generalnie sortowanie dziala, tzn sama funckja jest napisana dobrze.
    # Jedyne co stanowi problem to pozmienialy sie indexy jak przerabialem zapisywanie/czytanie pliku trzeba tu poprawic sciezke dostepu do listy ptk
    for index in range(len(leaderboard)):
        scores.append([leaderboard[index][0], int(leaderboard[index][5])])

    start = True

    while start:

        start = False

        for index in range(len(scores)-1):

            if scores[index][1] < scores[index+1][1]:

                scores[index][1], scores[index+1][1] = scores[index+1][1], scores[index][1]
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
    answer = input("Type any key to try again or '!' to get main menu. ")
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
