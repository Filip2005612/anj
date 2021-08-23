import random
import json
def check_file(board):
    with open('data/global.json', 'r') as f:
        data = json.load(f)
        lines = list(data[board].items())
        if len(lines) == 0:
            return True
def choose(board):
    with open('data/global.json', 'r') as f:
        data = json.load(f)

        lines = list(data[board].items())

        try:
            random_numbers = random.sample(range(len(lines)), 10)
        except:
            random_numbers = random.sample(range(len(lines)), len(lines))
        f.close()
        
        
    return random_numbers
            
                
                
def train(board, random_numbers, index, to_lan):
    print(random_numbers)
    with open('data/global.json', 'r') as f:
        data = json.load(f)
        lines = list(data[board].items())
        if to_lan == 'sk':
            question = lines[random_numbers[index]][0]
        if to_lan == 'en':
            question = lines[random_numbers[index]][1]
        f.close()
    
    return question
    
    
    
            










def check(index,random_numbers, answer, board, to_lan):
    with open('data/global.json', 'r') as f:
        data = json.load(f)
        lines = list(data[board].items())
        
        if to_lan == 'sk':
            right_answer = lines[random_numbers[index-1]][1]
        if to_lan == 'en':
            right_answer = lines[random_numbers[index-1]][0]
        
        print(right_answer)
        if right_answer == answer:
            return 1
        
        else:
            return right_answer


def next(self):
    global run
    next = input('Chces dalej pokracovat?: A/N/c ')
    if next.upper() == 'N':
        run = False
    if next.upper() == 'A':
        self.train()
        


