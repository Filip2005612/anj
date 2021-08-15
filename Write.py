from textblob import TextBlob
import json


def translate(word_to_trans, to_lan, from_lan, file):
    word = str(TextBlob(word_to_trans).translate(to = to_lan, from_lang= from_lan))

    if not check_word(word, file):
        append(word, word_to_trans, file, to_lan)

    return word


def append(word, text, file, language):
    with open('data/global.json', 'r+') as f:
        
        if language != 'sk':
            new = {word : text}
            data = json.load(f)
            data[file].update(new)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.close()
            
        else:
            new = {text : word}
            data = json.load(f)
            data[file].update(new)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.close()


def check_word( word, file):
    f = open('data/global.json')
    data = json.load(f)
    fi = data[file]

    for key in fi:
        if key == word:
            print('uz tu je')
            return True
        if fi[key] == word:
            print('uz tu je')
            return True
    return False


def create():
    try:
        
        f = open('data/global.json', 'r+')
        
        
    except:
        
        f = open('data/global.json', 'a')
        
        d = {}
        json.dump(d, f, indent= 2)
    f.close()
def new_file(file):
    f = open('data/global.json', 'r+')
    data = json.load(f)
    try:
        a = data[file]
    except:
        
        fl = {file : {}}
        data.update(fl)
        f.seek(0)
        json.dump(data, f, indent=2)