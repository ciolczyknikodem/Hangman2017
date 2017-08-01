import os, time


def load_countries_and_capitals():

    global a
    a = []

    for line in open("countries_and_capitals", 'r').readlines():
        temp = []
        temp.append(line.split(" | ")[0].upper())
        temp.append(line.split(" | ")[1].replace('\n', "").upper())
        a.append(temp)
        print(temp.__str__())

    print (time.strftime('%X %x'))


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
            ...
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


def main():
    # draw_menu_scene(False)
    load_countries_and_capitals()


if __name__ == '__main__':
    main()
