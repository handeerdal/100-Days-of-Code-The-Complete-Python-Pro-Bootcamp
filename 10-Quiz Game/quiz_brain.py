from data import question_data
from question_model import Question

class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    
    def checkanswer(self,givenanswer,actualanswer):
        if givenanswer==actualanswer:
            return 1


    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        answ=str(input(f'Q:{self.question_number} = {current_question.question}  True or False'))
        is_it_true=self.checkanswer(answ,current_question.answer)
        if is_it_true==1:
            self.score+=1
            print(f'True.Your Score {self.score}/{self.question_number}')
        else:
            print(f'Wrong.Your Score {self.score}/{self.question_number}')

    def still_has_questoions(self):
        return self.question_number<len(self.question_list)

