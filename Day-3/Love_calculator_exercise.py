
name1=input("enter name1")
name2=input("enter name2")
combined_name=name1+name2
combined_name_lower=combined_name.lower()

t=combined_name_lower.count('t')
r=combined_name_lower.count('r')
u=combined_name_lower.count('u')
e=combined_name_lower.count('e')

true=t+r+u+e

l=combined_name_lower.count('l')
o=combined_name_lower.count('o')
v=combined_name_lower.count('v')
e=combined_name_lower.count('e')

love=l+o+v+e

score=int(str(true)+str(love))
print(score)

if(score<10 or  score>90):
    print(f"your Score is {score} and you are like coke and mentos")
elif(score>=40 and score<=50 ):
    print(f"your Score is {score} and you are fine")
else:
    print(f"your Score is {score}")