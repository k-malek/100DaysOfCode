import pandas
import random
import pickle

class Card():
    cards=[]
    subjects={'front':None,'back':None}

    def __init__(self,words):
        self.side='front'
        self.words={'front':words[0],'back':words[1]}
        Card.cards.append(self)

    def flip_card(self):
        if self.side=='front':
            self.side='back'

        elif self.side=='back':
            self.side='front'
    
    def get_card_data(self):
        return self.side,self.words[self.side]
    
    @property
    def last_answer(self):
        return self._last_answer

    @last_answer.setter
    def last_answer(self,value):
        self._last_answer=value

    @classmethod
    def get_set(cls,csv_file):
        try:
            with open(f'data/{csv_file.split(".")[0]}.pickle') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return cls.create_set(csv_file)

            
    @classmethod
    def create_set(cls,csv_file):
        data=pandas.read_csv(f'data/{csv_file}',delimiter=';',encoding='utf-8')
        cls.set_subjects(data.columns)
        return [cls([data[data.columns[0]][i],data[data.columns[1]][i]]) for i in data.index] 
        
        
    @classmethod
    def set_subjects(cls,subjects):
        cls.subjects['front']=subjects[0]
        cls.subjects['back']=subjects[1]
        
    @classmethod
    def choose_new_card(cls):
        return random.choice(cls.cards) 