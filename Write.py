
import json
import socket
from kivy.network.urlrequest import UrlRequest
js = 'global.json'
un_js = "untranslated.json"

# def trans(self, *args):
#     url = "http://translate.pythonanywhere.com/t"

#     data = {"word":self.word.text, "to_lan":"sk", "from_lan":"en"}

#     headers = {'Content-type': 'application/json','Accept': 'text/plain'}

#     self.r = UrlRequest(url, req_body=json.dumps(data), req_headers=headers,on_success=self.get_success, on_failure=self.fail, on_error=self.fail)

# def get_success(self, *args):
#     self.test.text = str(self.r.result["word"])
#     print(self.r.result)

# def fail(self, *args):
#     print("f")
#     print(self.r.result)


def translate(word_to_trans, to_lan, from_lan, board):
    if not check_word(word_to_trans, board):
        word = 1
        append(word, word_to_trans, board, to_lan)
        return word
    else:
        return "uz tu je"

    


def append(word, text, board, language):
    with open(js, 'r+') as f:
        data = json.load(f) 
        fl = data[board]['words']
        to_lan = fl['to_lan']
        # from_lan = fl['from_lan']
        main_lan = fl['main_lan']
        if to_lan == main_lan:
            new = {word : {"translated": text, "right_answers": 0 }}
            data = json.load(f)
            data[board].update(new)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.close()
            
        else:
            new = {text : {"translated": word, "right_answers": 0}}
            data = json.load(f)
            data[board].update(new)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.close()


def check_word(word, board):
    f = open(js)
    data = json.load(f)
    fi = data[board]

    for key in fi:
        if fi[key]['translated'] == word:
            print('uz tu je slovenske')
            return True
        if key == word:
            print('uz tu je anglicke')
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
def create_register(file):
    try:
        
        f = open(file, 'r+')
        
    except:
        print('nie je tu')
        f = open(file, 'a')
    
        d = {"login": False, 'user':{}, "email":{}}
        json.dump(d, f, indent= 2)
    f.close()

def new_file(file,board, to_lan ,from_lan):
    f = open(file, 'r+')
    data = json.load(f)
    try:
        a = data[board]
        print('taka uz existuje')
        return 0
    except:
        
        fl = {board : {'to_lan': to_lan,
                        'from_lan':from_lan,
                        'main_lan':from_lan,
                        'words':{}
                }
            }
        data.update(fl)
        f.seek(0)
        json.dump(data, f, indent=2)
def enter_board(file, board):
    f = open(file, 'r')
    data = json.load(f)
    try:
        board = data[board]
        to_lan = board['to_lan']
        from_lan = board['from_lan']
        print('fungujem')
        f.close()
        return [to_lan, from_lan]
    except:
        f.close()
        return 0
def turn_langs(js, board):
    with open(js, 'r') as f:
        data = json.load(f)
        fl = data[board]
        TO = fl['to_lan']
        FR = fl['from_lan']
        fl['to_lan'] = FR
        fl['from_lan'] = TO   
        f.close()
    with open(js, 'w') as f:
        print(data)
        json.dump(data, f, indent=2)
        f.close()
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
def have_not_network(word, board, to_lan, from_lan):
    
    new_file(un_js,board, to_lan, from_lan)
    
    with open(un_js, 'r+') as f:
        data = json.load(f)
        new = {word:{
            "to_lan":to_lan,
            "from_lan": from_lan
        }}
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
            have_not_network(word_to_trans, board, to_lan, from_lan)
            return 0
        else:
            print('zadavas slovo v zlom jazyku')
            return 1

    



    
                
