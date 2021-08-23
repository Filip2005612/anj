from hashlib import new
from nltk.util import pr
from textblob import TextBlob
import json
import socket

def translate(word_to_trans, to_lan, from_lan, board):
    word = str(TextBlob(word_to_trans).translate(to = to_lan, from_lang= from_lan))

    if not check_word(word, board):
        append(word, word_to_trans, board, to_lan)

    return word


def append(word, text, board, language):
    with open('data/global.json', 'r+') as f:
        
        if language != 'sk':
            new = {word : text}
            data = json.load(f)
            data[board].update(new)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.close()
            
        else:
            new = {text : word}
            data = json.load(f)
            data[board].update(new)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.close()


def check_word(word, board):
    f = open('data/global.json')
    data = json.load(f)
    fi = data[board]

    for key in fi:
        if key == word:
            print('uz tu je')
            return True
        if fi[key] == word:
            print('uz tu je')
            return True
    return False


def create(file):
    try:
        
        f = open(file, 'r+')
        
        
    except:
        
        f = open(file, 'a')
        
        d = {}
        json.dump(d, f, indent= 2)
    f.close()
def new_file(file,board):
    f = open(file, 'r+')
    data = json.load(f)
    try:
        a = data[board]
    except:
        
        fl = {board : {}}
        data.update(fl)
        f.seek(0)
        json.dump(data, f, indent=2)



def alphabetcally(board):
    with open('data/global.json', 'r+') as f:

        data = json.load(f)


        fl = data[board]
        new_dict = {board:{}}
        for key, value in sorted(fl.items()):
            new_dict[board][key] = value
        
        # print(keys)
        #sor = sorted(fl.items(), key = lambda t: t[0])

        #sor = [word.lower() for word in str(keys).split()]
        # data[file] = new_dict
        # print(data[file])
        #a = json.dumps(fl ,sort_keys = True)
        json.dump(new_dict, f, indent = 2)





def checkInternetSocket(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        
        return False
def have_not_network(word, board):
    js = "data/untranslated.json"
    create(js)
    new_file(js, board)
    with open(js, 'r+') as f:
        data = json.load(f)
        new = {word:None}
        data[board].update(new)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.close()
    

def try_translate(word_to_trans, to_lan, from_lan, board):
    try:
        #backup(text)
        
        return translate(word_to_trans, to_lan, from_lan, board)
        
        
    except :
        if not checkInternetSocket():
            print("No internet")
            have_not_network(word_to_trans, board)
            return 0
        else:
            print('zadavas slovo v zlom jazyku')
            return 

    



    
                
