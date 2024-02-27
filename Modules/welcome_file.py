import datetime

def welcome_everyone():
    print('Welcome to Khwopa Mental Hostpital')
    name=input('Enter your name: ')
    return name


def greet(name):
    hr=datetime.datetime.now().hour
    if hr<12:
        print(f'Good Morning {name}')
    elif hr <17: 
        print(f'Good Afternoon {name}')
    else:
        print(f'Good Evening {name}')

# print(greet('apple'))
# welcome_everyone()
# print(greet('apple'))

if __name__=='__main__':
    name_of_person=welcome_everyone()
    greet(name_of_person)

