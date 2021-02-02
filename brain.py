class QuizBrain:
    def __init__(self, q_list):
        self.num = 0
        self.list = q_list

    def generate_question(self):
        current = self.list[self.num]
        self.num += 1
        user = input(f'Q.{self.num} {current.text} ').title()
        return user

    def next_question(self):
        for _ in self.list:
            self.generate_question()
        else:
            return False
