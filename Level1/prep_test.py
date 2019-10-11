def solution(answers):
    
    no1 = []
    no2 = []
    no3 = []
    count1 = 0
    count2 = 0
    count3 = 0
    
    # answers 길이만큼 수포자 1,2,3번의 정답 배열 생성
    
    for i in range(len(answers)):
        
        if i % 5 == 1:
            no1.append(2)
        elif i % 5 == 2:
            no1.append(3)
        elif i % 5 == 3:
            no1.append(4)
        elif i % 5 == 4:
            no1.append(5)
        else:
            no1.append(1)
        
        if i % 2 == 0:
            no2.append(2)
        else:
            if i % 8 == 1:
                no2.append(1)
            elif i % 8 == 3:
                no2.append(3)
            elif i % 8 == 5:
                no2.append(4)
            elif i % 8 == 7:
                no2.append(5)
            
        if i % 10 == 0 or i % 10 == 1:
            no3.append(3)
        elif i % 10 == 2 or i % 10 == 3:
            no3.append(1)
        elif i % 10 == 4 or i % 10 == 5:
            no3.append(2)
        elif i % 10 == 6 or i % 10 == 7:
            no3.append(4)
        else:
            no3.append(5)
    
    # answers와 1,2,3번의 정답 비교하며 맞은 문제 수 count
    
    for i in range(len(answers)):
        if answers[i] == no1[i]:
            count1 += 1
        if answers[i] == no2[i]:
            count2 += 1
        if answers[i] == no3[i]:
            count3 += 1
    
    # 맞은 문제 수 비교
    
    if count1 > count2 and count1 > count3:
        answer = [1]
    elif count2 > count1 and count2 > count3:
        answer = [2]
    elif count3 > count1 and count3 > count2:
        answer = [3]
    elif count1 == count2:
        if count1 > count3:
            answer = [1,2]
        else:
            answer = [1,2,3]
    elif count1 == count3:
        if count1 > count2:
            answer = [1,3]
        else:
            answer = [1,2,3]
    elif count2 == count3:
        if count2 > count1:
            answer = [2,3]
        else:
            answer = [1,2,3]
    else:
        answer = [1,2,3]
                
    return answer
