row = 5
col = 5

BINGO = [] #전체 빙고판
T = int(input()) #빙고 게임 수
for t in range (0, T) :
    for i in range (0, row) : #0부터 행 수까지 반복문
        row_input = input().split() # 행에 들어가는 숫자들 받아서 분리해서 저장.
        row_input = [int(j) for j in row_input]
        BINGO.append(row_input) #전체 빙고판에 위에 숫자들 추가한다.
    print (BINGO) #추가된 숫자들이 들어간 빙고판 프린트.

    input_numbers = input().split() #빙고판의 숫자들 맞추는 과정의 숫자들 받아서 분리해서 저장.
    input_numbers = [int(j) for j in input_numbers]

    count_of_input = 0  #빙고판의 숫자들 맞출 때 몇번째인지 세는 함수.

    for j in range (0, 75) :
        if BINGO[j] == input_numbers [j] :
            BINGO[j] = 0
            
    for number in input_numbers :
        count_of_input = count_of_input +1
        if rule1(number) == true :
            exit
        if rule2(number) == true :
            exit
        if rule3(number) == true :
            exit
        if rule4(number) == true :
            exit

    def rule1 ():
        if BINGO[number][0] == 0 or BINGO[number][1] == 0 or BINGO[number][2] == 0 or BINGO[number][3] == 0 or BINGO[number][4] == 0 :
        return ("true")
            
    def rule2 ():
        if BINGO[0] == 0 or BINGO[1] == 0 or BINGO[2] == 0 or BINGO[3] == 0 or BINGO[4] == 0 :
        return ("true")
            
    def rule3 ():
        if BINGO[0][0] == 0 and BINGO[1][1] and BINGO[2][2] and BINGO[3][3] and BINGO[4][4] :
        return ("true")
            
    def rule4 ():
        if BINGO[0][4] ==0 and BINGO[1][3]==0  and BINGO[2][2]==0  and BINGO[3][1]==0  and BINGO[4][0]==0 :
        return ("true")
        
             
        print (count_of_input)
 