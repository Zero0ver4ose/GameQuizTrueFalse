from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
'''question = Question(question_data["text"],question_data["answer"])
'''

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

question = QuizBrain(question_bank)

while question.still_has_questions():
    question.next_question()

print("You've completed the quiz")
print(f"Yout final score was: {question.score}/{len(question_bank)}")