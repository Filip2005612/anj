import random
import json
# import re

js = "global.json"
def check_file(board):
    with open(js, 'r') as f:
        data = json.load(f)
        lines = list(data[board]['words'].items())
        if len(lines) == 0:
            f.close()
            return True
            
        else: 
            f.close()
            return False
        
def choose(board):
    with open(js, 'r') as f:
        data = json.load(f)
        fl = data[board]['words']
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
            
                
                
    
def different_langs(word, board):
    with open(js, 'r') as f:
        data = json.load(f) 
        fl = data[board]
        to_lan = fl['to_lan']
        # from_lan = fl['from_lan']
        main_lan = fl['main_lan']
        if to_lan != main_lan:
            f.close()
            return word
            
        else:
            f.close()
            return fl['words'][word]['translated']
            
def check(question  ,answer, board):
    print(question)
    with open(js, 'r') as f:
        data = json.load(f) 
        fl = data[board]
        to_lan = fl['to_lan']
        # from_lan = fl['from_lan']
        main_lan = fl['main_lan'] 

         # with open('data/global.json', 'w') as fi:
        # if to_lan == 'sk':
        #     right_answer = fl[question]['translated']
            
        # if to_lan == 'en':
        #     
        if to_lan != main_lan:
            right_answer = fl['words'][question]['translated']
        if to_lan == main_lan:
            right_answer = question

        if right_answer == answer:
            with open(js, 'w') as fi:
                fl['words'][question]['right_answers'] += 1
                json.dump(data, fi, indent=2)
                fi.close()
                f.close()

            return 1
    

        else:
            # fi.close()
            f.close()
            return right_answer
        

    
        

def choose_with_brain(board):
    dict_words = {}
    list_words = []
    with open(js, 'r') as f:
        data = json.load(f)
        fl = data[board]
        to_lan = fl['to_lan']
        # from_lan = fl['from_lan']
        main_lan = fl['main_lan']
        lenght = 0
        for word in fl['words']:
            right_answers = fl['words'][word]['right_answers']
            
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
                    # if to_lan == main_lan:
                    list_words.append(i)
                    # else:
                    #     w = fl['words'][i]['translated']
                    #     list_words.append(w)
                
        find()

        f.close()
    print(list_words)
    return list_words




