import datetime
import operator

leader_board = []
scores = []

with open('Leaderboard', 'r') as f:

    for row in f:
        # print(row)
        leader_board.append(row.split())

# print (leader_board)

"""for index in range(len(leader_board)):
    scores[leader_board[index][0]] = leader_board[index][10]"""

for index in range(len(leader_board)):
    scores.append([leader_board[index][0], int(leader_board[index][10])])

print(scores)

start = True
while start:
    start = False
    for index in range(len(scores)-1):
        if scores[index][1] < scores[index+1][1]:
            scores[index][1], scores[index+1][1] = scores[index+1][1], scores[index][1]
            start = True

print(scores)



"""score = leader_board[1][10]

print(score)"""


# current_date = datetime.date.today()

# print(current_date)

# name | date | guessing_time | guessing_tries | guessed_word | score
