from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text=question['text']
    question_answer=question['answer']
    new_question=Question(question_text,question_answer)#new_question is an object of class Question
    question_bank.append(new_question)#now the onj have all the data

quiz=QuizBrain(question_bank)

while(quiz.still_have_questions()):
    quiz.next_question()
