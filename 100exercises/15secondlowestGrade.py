def minScore(students):
    min_score = float('inf')
    
    for student in students:
        score = student[1]
        if score < min_score:
            min_score = score
    return min_score
            
if __name__ == '__main__':
    students = []
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    min_score = minScore(students)
    
    for i in students:
        if i[1] != min_score:
            result.append(i)
            
    result.sort(key=lambda x: x[0])
    
    min_score = minScore(result)
    
    for i in result:
        if min_score == i[1]:
            print(i[0])
        
        