# Imports
from question import Question
from data import question_data

# Create Question objects
question_info = []
for info in question_data:
    q = info['text']
    a = info['answer']
    question_info.append(Question(q, a))


print(question_info)
