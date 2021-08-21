def solution(numbers):
    answer = 0

    temp = []        #문자열 값의 정수변환 및 정렬을 위한 list 선언
    max_str = ''     # 주어진 numbers로 조합할 수 있는 max 숫자의 str 타입 형
    max_int = 0      # 주어진 numbers로 조합할 수 있는 max 숫자의 int 타입 형

    # numbers의 값들을 temp list 에 정수변환 하여 넣음
    for i in range(len(numbers)):
        temp.append(int(numbers[i]))

    # temp list 를 내림차순 정렬함
    temp.reverse()

    # list 에 있는 값들을 하나씩 꺼내 max_str에 붙임
    for j in temp:
        max_str += str(j)

    # max_str 을 int 로 캐스팅
    max_int = int(max_str)

    # 소수 개수 찾기
    for x in range(2,max_int+1):
        for y in range(1,x):
            if y == 1 :  # 분모가 1이면 continue
                continue

            if x%y == 0 : # 나누어 떨어지는 수가 있다면 넘어감
                continue

        if y == x-1 :
             print("x : ",x)
             answer += 1  # 1 제외하고 나누어 떨어지는 수가 없었다면 소수 이므로 count 1 올림



    return answer



numbers1 = "17"
numbers2 = "011"

print("First Answer : ",solution(numbers1))
print("Second Answer : ", solution(numbers2))



