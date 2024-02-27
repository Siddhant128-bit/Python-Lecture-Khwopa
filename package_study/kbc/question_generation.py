def generate_questions():
    num_of_questions=int(input('Enter number of questions: '))
    question_list=[]
    answers_list=[]
    for question in range(0,num_of_questions):
        question_list.append(input(f'Enter {question+1} question: '))
        answers_list.append(input(f'Enter {question+1} answer: '))
    
    question_answers=dict(zip(question_list,answers_list))
    return question_answers

if __name__=='__main__':
    generate_questions()