import datetime

with open('Leaderboard', 'r') as f:
    reader = f.read()

print (reader)

current_date = datetime.date.today()

print(current_date)
