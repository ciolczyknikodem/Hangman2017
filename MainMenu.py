import os
import time
import random


def load_countries_and_capitals():

    # global capital_list
    capital_list = []

    for line in open("countries_and_capitals", 'r').readlines():
        temp = []
        temp.append(line.split(" | ")[0].upper())
        temp.append(line.split(" | ")[1].replace('\n', "").upper())
        capital_list.append(temp)
        # print(temp.__str__())

    # print (time.strftime('%X %x'))

    return capital_list


def draw_menu_scene(badAnswer):

    os.system('clear')
    scene = open("MainMenuScene", 'r').readlines()

    for line in scene:
        print (line, end='')

    while(True):
        choice = None
        if badAnswer == False:
            choice = input("Your Choice: ")
        if badAnswer == True:
            choice = input("Bad Choice, Try Again: ")
        if choice == "1":
            global guessingTime
            guessingTime = time.time()
        elif choice == "2":
            ...
        elif choice == "3":
            ...
        elif choice == "4":
            draw_quit_scene()
            exit()

        else:
            draw_menu_scene(True)


def draw_quit_scene():

    os.system('clear')
    scene = open("GameQuitScene", 'r').readlines()

    for line in scene:
        print (line, end='')


def pick_random_capital(capital_list):

    GuessingCapitalCountry = []
    GuessingCapitalCountry.append(random.choice(capital_list))

    return GuessingCapitalCountry


def change_capital_to_dash(guessing_capital):

    guessing_list = []

    for x in guessing_capital:
        pass


def main():

    # draw_menu_scene(False)
    capital_list = load_countries_and_capitals()
    GuessingCapitalCountry = pick_random_capital(capital_list)
    print(GuessingCapitalCountry)


if __name__ == '__main__':
    main()



def random_pick_capital():
    pass # Nikodem, funkcja pobiera liste panstw losuje i zwraca jedno panstwo i maisto,|| Argument: lista panstw ||  Return liste
    """DONE"""

def stage():
    pass # Kamil, ekran glowny wyswietlanie life, time i asci art hangman, wykorzystane litery
    for line in open("MainGameScene", 'r').readlines():
        if line.__contains__("%LIVES") and line.__contains__("%TIME"):
            ActualTime = time.time()
            line.replace("%LIVES", lifes())
            timeDifference = guessingTime - ActualTime
            line.replace("%TIME", timeDifference)
        if line.__contains__("%TRIES"):
            line.replace("%TRIES", tries)
        if line.__contains__("%GUESSED"):
            line.replace("%GUESSED", guessed)




def dash():
    pass # Tablica dwuindeksowa, pierwszt indeks = stolica, a drugi funckaj zamienia stolice na _, argument stolica, return liste stringow

def lifes():
    pass # Funkcja pobiera info o tym czy zgadujesz miasto czy litere i w zaleznosci od tego odejmuje zycia, zwraca informacje jesli zostalo jedno zycie, return zmienna

def hint():
    pass # Funkcja pobiera parametr/argument o ostatnim zyciu i zwraca informacje do stage o printowaniu podpowiedzi w postaci Panstwa, argument zmienna life, return string nazwa panstwa

def check_if_asnwer_correct():
    global tries
    global guessed
    pass # Funkcja pobiera informacje o lieterze/slowie uzytkowinika i podmienia _ w zgadywanym miescie na litery, argument zgadywana stolica, return liste stringow

def winner_name():
    pass # Funkcja || Argument: True/False || Return stringow

def highscore():
    pass # Funkcja po zakonczeniu gry oblicza ptk ktore uzyskal uzytkowinik, || Argumenty: czas/date, zycia, proby odgadniecia, imie || Return: liste stringow do zapisu

def end_stage_succes():
    pass # Funkcja printuje tablice wyniku innych graczy, pobiera z pliku info, wylicza ktore miejsce zajales || Argumnet: list highscore || Return Liste wszystkich wynikow np top 10

def save_highscore():
    pass # Pobiera info od end_stage i zapisuje do pliku info juz z nowym graczem || Argument: list highscore || Return None

def lose_stage():
    pass # Funkcja printuje ekran przegranej i pyta o ponowna gre || Argument: lifes || Return None
