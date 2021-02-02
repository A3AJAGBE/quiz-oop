# Imports
from question import Question
from data import question_data
from brain import QuizBrain

print('The question are either "True" or "False".')

# Create Question Instance
question_info = []
for info in question_data:
    q = info['text']
    a = info['answer']
    question_info.append(Question(q, a))

# Quiz brain Instance
quiz_brain = QuizBrain(question_info)
quiz_brain.generate_question()
