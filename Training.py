import random
import json
import re
def check_file(board):
    with open('data/global.json', 'r') as f:
        data = json.load(f)
        lines = list(data[board].items())
        if len(lines) == 0:
            f.close()
            return True
            
        else: 
            f.close()
            return False
        
def choose(board, to_lan):
    with open('data/global.json', 'r') as f:
        data = json.load(f)
        fl = data[board]
        lenght = 0
        list_words = []
        for word in fl:
            
            list_words.append(word)
            
            lenght += 1
        

        try:
            list_words = random.sample(list_words, 10)
        except:
            list_words = random.sample(list_words, lenght)
        f.close()
        
    
    return list_words
            
                
                
    
def different_langs(word, board, to_lan):
    with open('data/global.json', 'r') as f:
        
        if to_lan == 'sk':
            f.close()
            return word
            
        if to_lan == 'en':
            data = json.load(f)
            fl = data[board]
            f.close()
            return fl[word]['translated']
            
def check(question  ,answer, board, to_lan):
    print(question)
    with open('data/global.json', 'r') as f:
        data = json.load(f) 
        fl = data[board]
        # with open('data/global.json', 'w') as fi:
        if to_lan == 'sk':
            right_answer = fl[question]['translated']
            
        if to_lan == 'en':
            right_answer = question
            
        if right_answer == answer:
            with open('data/global.json', 'w') as fi:
                fl[question]['right_answers'] += 1
                json.dump(data, fi, indent=2)
                fi.close()
                f.close()

            return 1
    

        else:
            # fi.close()
            f.close()
            return right_answer
        

    
        

def choose_with_brain(board, to_lan):
    dict_words = {}
    list_words = []
    with open('data/global.json', 'r') as f:
        data = json.load(f)
        fl = data[board]
        lenght = 0
        for word in fl:
            right_answers = fl[word]['right_answers']
            
            dict_words[word] = right_answers
            lenght += 1

        if lenght > 10:
            lenght = 10
        
        def find(r = lenght):
            d2 = {}
            rest = r
            for k, v in dict_words.items():
                d2.setdefault(v, []).append(k)
            res = d2[min(d2)]
            rest -= len(res)
            if rest > 0:
                
                print(rest)
                l = random.sample(res, len(res))
                for i in l:
                    del dict_words[i]
                    
                    list_words.append(i)

                print(dict_words)

                find(r= rest)
            else:
                r = random.sample(res, len(res) + rest)
                for i in r:
                    if to_lan == 'sk':
                        list_words.append(i)
                    if to_lan == 'en':
                        w = fl[i]['translated']
                        list_words.append(w)
                
        find()

        f.close()
    print(list_words)
    return list_words




