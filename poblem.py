# 1. Write a Python program to sum all the items in a list.
sum_list =[10,20,25]
sum1=0
for i in sum_list:
    sum1 += i
print(sum1)

# 2. Write a Python program to multiplies all the items in a list. 
sum_list =[10,5,2]
sum1=1
for i in sum_list:
    sum1 *= i
print(sum1)

# 3. Write a Python program to get the largest number from a list.
listmax =[2,5,8,0]
max =0
for i in listmax:
    if i > max:
        max=i
print(max)