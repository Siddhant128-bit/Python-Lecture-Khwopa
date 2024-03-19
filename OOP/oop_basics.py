'''
class vs object 

class = animal 
object = dog 

class= vehicle 
object = car,bike,Truck 

class= car
object = mercedes, bmw, ferari 

'''


class calculator:
    #function 1 addition
    def addition(a,b):
        return a+b
    
    def subtraction(a,b):
        return a-b
    
    def division(a,b):
        return a/b 
    
    def multiplication(a,b):
        return a*b
    

#get user input 
calculate=calculator
print(calculate.subtraction(5,4))

    