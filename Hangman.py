import os


def open_file():

    all_capitals = []

    with open('countries_and_capitals.txt') as f:
        capitals = f.readlines()

        for x in capitals:
            print(x.split(' | '))

            for y in x:
                capitals.append(y)

            print(x)
            print(all_capitals)


def main():
    os.system('clear')
    open_file()


if __name__ == '__main__':
    main()
