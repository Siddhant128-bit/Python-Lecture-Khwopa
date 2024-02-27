#import kbc
from kbc.question_generation import generate_questions
from kbc.check_answers import validate_answers

questions=generate_questions()

for question in questions:
    print(question)
    user_answer=input('Enter Your answer: ')
    actual_answer=questions[question]
    results=validate_answers(user_answer,actual_answer)
    if results==False:
        print("Game Over")
        break
    