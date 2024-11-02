from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for i in range(0,len(question_data)):
     question=Question(question_data[i]['text'],question_data[i]['answer'])
     question_bank.append(question)
   
# for i in range(0,len(question_bank)):
#     print(question_bank[i].answer)

quiz=QuizBrain(question_bank)


while (quiz.still_has_questoions()):
    quiz.next_question()
    print('\n')

print(f'You finished the game final score: {quiz.score}/{len(quiz.question_list)} ')

     
