student_height = (input().split())
height=0
for i in range(0,len(student_height)):
    height += int(student_height[i])
    
count=0
for i in range(0,len(student_height)):
    count=count+1

avg_height=height/count

print(round(avg_height))
    