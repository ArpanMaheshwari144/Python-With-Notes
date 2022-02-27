def game():
    return 200

score = game()

with open('text/hiscore.txt', 'r') as f:
    hiScoreStr = f.read()

if hiScoreStr=='':
    with open('text/hiscore.txt', 'w') as f:
        f.write(str(score))

elif int(hiScoreStr)<score:
    with open('text/hiscore.txt', 'w') as f:
        f.write(str(score))