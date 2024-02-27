def add_2_numbers(a,b):
    return a+b

list_of_num=[]

#Problem 1 list form garne 
num_of_elements=int(input('Enter number of elements: '))
for i in range(num_of_elements):
    list_of_num.append(int(input(f'Enter {i+1} element: ')))

sum=0
for element in list_of_num:
    sum=add_2_numbers(sum,element)

print(sum)
