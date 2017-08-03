from collections import OrderedDict
global leaderboard ; leaderboard = []
global scores ; scores = OrderedDict()

def saves_score_string(name, date, guessing_time, guessing_tries, guessed_word, score):
    string = str('{}|{}|{}|{}|{}|{}'.format(name, date, guessing_time, guessing_tries, guessed_word, score))
    with open("Leaderboard2", 'a') as f:
        f.write(string + '\n')
        f.close()

def calculate_scores():
    if len(leaderboard) == 0:
        for line in open("Leaderboard2", 'r').readlines(): leaderboard.append(line)
    temp_dict = {}
    scores.clear()
    for x in leaderboard:
        try:
            x = str(x).split("|")
            y = x[5].replace('\n', '')
            temp_dict.__setitem__(x[0], y)
        except:
            continue
    res = list(sorted(temp_dict, key = temp_dict.__getitem__, reverse = True))
    if len(res) == 0:
        return
    i = 0
    n = 10
    if len(res) < 10:
        n = len(res)
    while(i < n):
        scores.__setitem__(res[i], temp_dict.__getitem__(res[i]))
        i+=1

def print_leaderboard():
    if len(scores) > 0:
        for key in scores.keys():
            print(key + ": " + scores.get(key))

saves_score_string("arka", "gdynia", "kurwa", "świnia", "XD", 123123123)
saves_score_string("arka2", "gdynia", "kurwa", "świnia", "XD", 1231231232)
saves_score_string("test", "test2", "test3", "test4", "test", 123)
calculate_scores()
print_leaderboard()

