import os
import time
import random
import datetime
import operator

global capitals_list; capitals_list = []
global tries; tries = 0
global guessed; guessed = []
global costume_state;
global lifes;
global dash_capital; dash_capital = []


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
            ...
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
                line = line.replace("%HINT", hint(lifes, GuessingCapitalCountry))   # Nie wiem czy bedzie potrzebny parametr do wywolania funkcji, ewentualnie do poprawy

            print (line)
        if(lifes <= 0): # sprawdza czy uzytkownik przegrał
            print("You have run out of your lives!")
            time.sleep(1)
            exit()
        if(str(dash_capital).__contains__("_") == False): #sprawdza czy użytkownik wygrał
            print("You won")
            time.sleep(1)
            exit()
        check_if_asnwer_correct(GuessingCapitalCountry)


def check_if_asnwer_correct(guessing_capital):

    # Funkcja pobiera informacje o lieterze/slowie uzytkowinika i podmienia _ w zgadywanym miescie na litery, argument zgadywana stolica, return liste stringow
    capital = str(guessing_capital[1]).upper().replace(" ", '')
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
    if(answer.isalpha() and answer.__len__() > 1):
        # print("capital: " + capital)
        # print("answer: " + answer)
        # exit()

        if(capital == answer):
            globals().__setitem__("dash_capital", answer)
        else:
            global  costume_state,lifes
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


def open_leaderboard():

    leaderboard = []

    with open('Leaderboard', 'r') as f:

        for row in f:
            print(row)
            leaderboard.append([row])

    return leaderboard


def highscore(lifes, time, tries, guessing_word, name, leaderboard):

    highscore = []
    current_date = datetime.date.today()

    score = 100 + (lifes * 10) - (tries * 5) - (round(time, 2))

    highscore.append(name)
    highscore.append(" | ")
    highscore.append(current_date)
    highscore.append(" | ")
    highscore.append(time)
    highscore.append(" | ")
    highscore.append(tries)
    highscore.append(" | ")
    highscore.append(guessing_word)
    highscore.append(" | ")
    highscore.append(score)

    leaderboard.append(highscore)

    return leaderboard


def save_highscore(scores):
    """ Argument: List
        Return: None

        Function save scores to file"""

    with open('Leaderboard', 'w') as f:
        f.write(scores)


def calculate_position(leaderboard):
    """ Argument: List
        Return: List

        Function use bubble sort to sorting list of players scores"""

    scores = []

    for index in range(len(leaderboard)):
        scores.append([leaderboard[index][0], int(leaderboard[index][10])])

    start = True

    while start:

        start = False

        for index in range(len(scores)-1):

            if scores[index][1] < scores[index+1][1]:

                scores[index][1], scores[index+1][1] = scores[index+1][1], scores[index][1]
                start = True

    return scores


def hint2():
    pass # Funkcja pobiera parametr/argument o ostatnim zyciu i zwraca informacje do stage o printowaniu podpowiedzi w postaci Panstwa, argument zmienna life, return string nazwa panstwa


def winner_name2():
    pass # Funkcja || Argument: True/False || Return stringow

def highscore():
    pass # Funkcja po zakonczeniu gry oblicza ptk ktore uzyskal uzytkowinik, || Argumenty: czas/date, zycia, proby odgadniecia, imie || Return: liste stringow do zapisu

def end_stage_succes():
    pass # Funkcja printuje tablice wyniku innych graczy, pobiera z pliku info, wylicza ktore miejsce zajales || Argumnet: list highscore || Return Liste wszystkich wynikow np top 10

def save_highscore():
    pass # Pobiera info od end_stage i zapisuje do pliku info juz z nowym graczem || Argument: list highscore || Return None

def lose_stage():
    pass # Funkcja printuje ekran przegranej i pyta o ponowna gre || Argument: lifes || Return None


def main():
    load_countries_and_capitals()
    draw_menu_scene()


if __name__ == '__main__':
    main()
