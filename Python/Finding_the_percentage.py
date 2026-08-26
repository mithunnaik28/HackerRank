if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for keys,valuse in student_marks.items():
        if keys==query_name:
            answer=sum(valuse)/3
            print(f"{answer:.2f}")
    
    
