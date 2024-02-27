'''
def sum_of_numbers(a,b,c):
    return a+b+c


sum=sum_of_numbers(1,2,3,4)
print(f'sum of 3 numbers: {sum}')
'''
'''
def sum_of_numbers(*numbers):
    # print(sum(numbers))
    return len(numbers),sum(numbers)

#start time here
num_of_elements,total_of_elements=sum_of_numbers(1,2,3,4,5)
#end time here
print(f'Sum of {num_of_elements} numbers is : {total_of_elements}')
#end time- start time = total time of function
'''
#Kwargs understanding 

''' 
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 # Driver code
myFun(first='Siddhant', mid='Prasad', last='Sharma')

'''
'''
def database(first_name,mid_name,last_name):
    keys=['first_name','mid_name','last_name']
    values=[first_name,mid_name,last_name]
    working_dictionary=dict(zip(keys,values))
    print(working_dictionary)

def database(**data_to_store):
    return data_to_store

print(database(first_name='Siddhant',mid_name='Prasad',last_name='Sharma'))
#database('Aishwariya','Salman','Khan')

'''

# def sum_of_numbers(parameter_list):
#     pass




# total_of_list=sum_of_numbers([1,2,3,4])
# print(total_of_list)

import random

non_value=[38,48]

while True:
    random_val=random.randrange(1,49)
    if random_val not in non_value:
        break

print(random_val)