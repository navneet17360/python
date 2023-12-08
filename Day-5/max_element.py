#bubble sort method
student_scores=list(map(int,input().split()))

for i  in range(0,len(student_scores)):
    for j in range(0,len(student_scores)-i-1):
        if(student_scores[j]>student_scores[j+1]):
             temp=student_scores[j]
             student_scores[j]=student_scores[j+1]
             student_scores[j+1]=temp




print(student_scores[-1])
