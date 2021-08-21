def solution(answers):
    length = len(answers)
    player1_answ = [1,2,3,4,5]
    player2_answ = [2,1,2,3,2,4,2,5]
    player3_answ = [3,3,1,1,2,2,4,4,5,5]
    players_answ = [player1_answ,player2_answ,player3_answ]
    players_finansw = []
    for i in players_answ:
        x,y = get_quotient_remainder(length,len(i))
        fin_answ = []
        if x != 0 and y!=0:
            fin_answ = x*i.append(i[:y])
        elif x!=0 and y == 0:
            fin_answ = x*i
        elif x==0 and y!=0:
            fin_answ = i[:y]
        players_finansw.append(fin_answ)
    corrects = []
    for j in players_finansw:
        correct = 0
        for k in range(length):
            if answers[k] == j[k]:
                correct+=1
        corrects.append(correct)
    Max = max(corrects)
    players = []
    for i in range(len(corrects)):
        if corrects[i] == Max:
            players.append(i+1)
    players.sort()
    return players

def get_quotient_remainder(x,y):
    return x//y , x%y

answerss = [1,3,2,4,2]

print(solution(answerss))