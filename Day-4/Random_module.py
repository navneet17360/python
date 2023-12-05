#Randomisation or random module

import random
#import my_module

random_number=random.randint(100,200)
print(random_number)
#print(my_module.pi)
  
random_float=random.random()*5
#gives number between 0 and 1 but not 1
#if i multiply by it 5 then it will give me number between 0 and 5 but not 5
#.00000... to 4.9999999
print(random_float)

love_score=random.randint(1,100)
print(f"your Score is {love_score}")