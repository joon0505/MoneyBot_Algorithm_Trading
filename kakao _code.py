ChkandQue = input('')
ChkandQue_split = ChkandQue.split()
NumOfChkpo = int(ChkandQue_split[0])
NumOfQues = float(ChkandQue_split[1])

CheckPoints = []
for i in range(NumOfChkpo):
    chkpoint = input('')
    chkpoint_split = chkpoint.split()
    chkpoint_split[0] = int(chkpoint_split[0])
    chkpoint_split[1] = int(chkpoint_split[1])
    CheckPoints.append(chkpoint_split)



def Question_with_No_HP(question):
    possibility = False
    start_index = question[0]

    starting_point = CheckPoints[start_index-1]

    end_index = question[1]

    ending_point = CheckPoints[end_index-1]

    if starting_point[0] == ending_point[0]:
        possibility = True
        return possibility
    elif starting_point[1] == ending_point[1]:
        possibility = True
        return possibility
    else:
        for i in range(len(CheckPoints)):

            if i == start_index-1:
                continue
            elif starting_point[0] == CheckPoints[i][0]:
                question[0] = i+1
                return Question_with_No_HP(question)
            elif starting_point[1] == CheckPoints[i][1]:
                question[0] = i+1
                return Question_with_No_HP(question)
            else :
                return possibility

def Question_with_HP(starting_point, ending_point ,HP,boost):
    possibility = False
    if (starting_point[0] == ending_point[0]) and boost == True:
        boost = False
        possibility = True
        return possibility

    elif (starting_point[1] == ending_point[1]) and boost == True:
        boost = False
        possibility = True
        return possibility
    else:
        for i in range(len(CheckPoints)):
            if abs(starting_point[0]-CheckPoints[i][0]) <= HP and abs(starting_point[0]-CheckPoints[i][0]) > 0 :
                starting_point[0] = CheckPoints[i][0]
                HP = HP - abs(starting_point[0]- CheckPoints[i][0])
                return Question_with_HP(starting_point,ending_point,HP,boost)
            elif  abs(starting_point[1]-CheckPoints[i][1]) <= HP and abs(starting_point[1]-CheckPoints[i][1]) > 0 :
                starting_point[1] = CheckPoints[i][1]
                HP = HP - abs(starting_point[1]- CheckPoints[i][1])
                return Question_with_HP(starting_point,ending_point,HP,boost)
            else :
                continue

        return False

Questions = []
for i in range(NumOfQues):
    question = input('')
    question_split = question.split()
    question_split[0] = int(question_split[0])
    question_split[1] = int(question_split[1])
    question_split[2] = int(question_split[2])
    Questions.append(question_split)

    if Questions[i][2] == 0:
        result1 = Question_with_No_HP(Questions[i])
        if result1 == True:
            print('YES')
        else:
            print('NO')
    else:
        start_index = Questions[i][0]
        end_index = Questions[i][1]
        HP = Questions[0][2]
        starting_point = CheckPoints[start_index-1]
        ending_point = CheckPoints[end_index-1]
        result2 = Question_with_HP(starting_point,ending_point,HP,True)
        if result2 == True:
            print('YES')
        else:
            print('NO')































