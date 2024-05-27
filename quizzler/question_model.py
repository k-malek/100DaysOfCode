import requests
from html import unescape

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    @staticmethod
    def get_questions(amount=10):
        amount = amount if amount>0 else 1
        response = requests.get('https://opentdb.com/api.php',
                                params={'amount':str(amount),'type':'boolean'},
                                timeout=5000)
        response.raise_for_status()
        question_data=response.json()['results']

        question_bank = []
        for question in question_data:
            question_text = unescape(question["question"])
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        
        return question_bank