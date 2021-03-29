def solution(array, commands):
    
#    answer = []
#    
#    for v in commands:
#        if v[0] == 1:
#            narray = array[:v[1]]
#            narray.sort()
#            if v[2] == 1:                
#                answer.append(narray[0])
#            else:
#                answer.append(narray[v[2]-1])
#        else:
#            narray = array[v[0]-1:v[1]]
#            narray.sort()
#            if v[2] == 1:
#                answer.append(narray[0])
#            else:
#               answer.append(narray[v[2]-1])
#    
#    return answer

    answer = []
    
    for c in commands:
        answer.append(sorted(array[c[0]-1:c[1]])[c[2]-1])
        
    return answer
