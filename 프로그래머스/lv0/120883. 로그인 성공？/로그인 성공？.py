def solution(id_pw, db):
    answer = 'fail'
    
    for data in db:
        if data[0] == id_pw[0]:
            answer = 'wrong pw'
            
            if data[1] == id_pw[1]:
                answer = 'login'
                
                break
    
    return answer