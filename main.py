from quiz_interface import QuizInterface
from data import question_data
from question_model import Question
from app_brain import QuizBrain

# main file
question_bank=[]
for question in question_data:
        question_text=question["question"]
        question_answer=question["correct_answer"]
        new_question=Question(question_text,question_answer)
        question_bank.append(new_question)

qb=QuizBrain(question_bank)
ui=QuizInterface(qb)
while qb.still_has_questions():
       qb.get_next_question()