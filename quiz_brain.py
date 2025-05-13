class QuizzBrain:

    def __init__(self, question_list):
        self.quest_no = 0
        self.quest_list = question_list
        self.score = 0

    def still_has_questions(self):
        list_length = len(self.quest_list)
        return self.quest_no < list_length

    def next_question(self):
        current_question = self.quest_list[self.quest_no]
        self.quest_no += 1
        user_answer = input(f'Q.{self.quest_no} {current_question.text} (True/False): ').lower().strip()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # check if the user's answer is same as correct answer and tells them if they got it or not
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('Sorry, you got it wrong!')
        print(f'The correct answer is: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.quest_no}')
        print('\n')