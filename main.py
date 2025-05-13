from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']

    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz_brain = QuizzBrain(question_bank)

print('Welcome to the Quiz game program!')
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f'Thanks for playing🤗, The game has ended')
print(f'Your final score is {quiz_brain.score}/{quiz_brain.quest_no}')