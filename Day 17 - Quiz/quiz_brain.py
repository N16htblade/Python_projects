class QuizBrain:

    def __init__(self, question_list):
         self.question_number = 0
         self.question_list = question_list
         self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False

    def next_question(self):
        question_text = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {question_text.text}. (True/False)?: ")
        self.check_answer(user_answer, question_text.answer)

    def check_answer(self, u_answer, q_answer):
        if u_answer.lower() == q_answer.lower():
            self.score += 1
            print (f"You got it right!")
        else:
            print ("That's wrong.")
        
        print (f"The correct answer was: {q_answer}")
        print (f"Your current score is: {self.score}/{self.question_number}\n")