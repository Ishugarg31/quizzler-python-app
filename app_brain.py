from data import question_data
from question_model import Question
import html

class QuizBrain:
        def __init__(self,question_bank):
                self.question_number=0
                self.question_list=question_bank    
                self.score=0
                     
        def get_next_question(self):
            self.current_question=self.question_list[self.question_number]
            self.question_number+=1
            return f"Q.{self.question_number}:{html.unescape(self.current_question.question_text)}"
        #     user_answer=input(f"Q.{self.question_number}:{html.unescape(current_question.question_text)} (True/False)")
            #print(current_question.correct_answer)
        #     self.check_answer(user_answer,current_question.correct_answer)

        def still_has_questions(self):
               return self.question_number < len(self.question_list)
        
        def check_answer(self,user_answer):
               correct_answer= self.current_question.correct_answer
               if user_answer.lower()==correct_answer.lower():
                      self.score+=1
                      return True
               else :
                      return False
               
               #print(f"your score is {self.score}/{self.question_number}")    
        
                      

