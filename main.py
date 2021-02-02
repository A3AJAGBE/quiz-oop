# Imports
from question import Question
from data import question_data
from brain import QuizBrain

print('Type "True" or "False" to answer the following questions.')

# Create Question Instance
question_info = []
for info in question_data:
    q = info['text']
    a = info['answer']
    question_info.append(Question(q, a))

# Quiz brain Instance
quiz_brain = QuizBrain(question_info)

# Iterate through the questions
while quiz_brain.next_question():
    quiz_brain.generate_question()
