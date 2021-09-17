import json
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import Write
import Training
from kivy.network.urlrequest import UrlRequest
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel

js = "global.json"
un_js = "untranslated.json"

Write.create(js)
Write.create(un_js)

board = ""
to_lan = "sk"
from_lan = "en"

#APP CLASSES
class NameWindow(Screen):
    name_of_user = ObjectProperty(None)
    def btn(self):
        pass

    # UPLOAD TO DATABSE
    def upload(self):
        with open(js, "r") as f:
            words = json.load(f)
        url = "http://wordappproject.pythonanywhere.com/w"
        # url = "http://127.0.0.1:5000/w"
        raw_data = {"type":"upload" ,"data":json.dumps(words), "name":str(self.name_of_user.text)}
        data = json.dumps(raw_data)
        headers = {'Content-type': 'application/json','Accept': 'text/plain'}
        self.r = UrlRequest(url, req_body=data, req_headers=headers,on_success=self.get_upload_success,on_error=self.get_upload_err, on_failure=self.get_upload_err)

    def get_upload_success(self, *args):
        print("Uploaded successfully")
        print(self.r.result)

    def get_upload_err(self, *args):
        print("error")
        try:
            print(self.r.result)
        except:
            print("idk")

    # DOWNLOAD FROM DATABSE
    def download(self):
        url = "http://wordappproject.pythonanywhere.com/w"
        # url = "http://127.0.0.1:5000/w"
        raw_data = {"type":"download" ,"data":"nothing", "name":str(self.name_of_user.text)}
        data = json.dumps(raw_data)
        headers = {'Content-type': 'application/json','Accept': 'text/plain'}
        self.r = UrlRequest(url, req_body=data, req_headers=headers,on_success=self.get_download_success,on_error=self.get_download_err, on_failure=self.get_download_err)

    def get_download_success(self, *args):
        print("Downloaded successfully!")
        data = self.r.result["data"]
        with open(js, "w") as f:
            json.dump(data, f, indent=2)

    def get_download_err(self, *args):
        print("error")
        try:
            print(self.r.result)
        except:
            print("idk")

    # DELETE FROM DATABSE
    def delete(self):
        url = "http://wordappproject.pythonanywhere.com/w"
        # url = "http://127.0.0.1:5000/w"
        raw_data = {"type":"delete" ,"data":"nothing", "name":str(self.name_of_user.text)}
        data = json.dumps(raw_data)
        headers = {'Content-type': 'application/json','Accept': 'text/plain'}
        self.r = UrlRequest(url, req_body=data, req_headers=headers,on_success=self.get_delete_success,on_error=self.get_delete_err, on_failure=self.get_delete_err)

    def get_delete_success(self, *args):
        print("Deleted successfully!")
        print(self.r.result)

    def get_delete_err(self, *args):
        print("error")
        try:
            print(self.r.result)
        except:
            print("idk")


class AskWindow(Screen):
    f = ObjectProperty(None)
    to = ObjectProperty(None)
    from_lan = ObjectProperty(None)
    #DETERMINE FUNDAMENTAL INFORMATIONS
    def btn(self):
        global board, to_lan, from_lan
        board = self.f.text
        to_lan = self.to.text
        from_lan = self.from_lan.text

        # if to_lan == '':
        #     print('nezadal si jazyk')
        # elif from_lan == '':
        #     print('nezadal si jazyk')
        # else:
        kv.current = "mode"
        kv.transition.direction = "left"
        Write.new_file(js, board)


class ModeWindow(Screen):
    #OPEN TRAIN WINDOW
    def train(self):
        if not Training.check_file(board):
            print('idem trenovat')
            TrainWindow.words = Training.choose(board, to_lan)
            kv.current = "train"
            kv.transition.direction = "left"
        else:
            print('kniznica nema ziadne slovicka')
    #OPEN TRAIN WITH BRAIN WINDOW
    def train_with_brain(self):
        if not Training.check_file(board):
            print('idem trenovat')
            Train_with_brain_window.words = Training.choose_with_brain(board, to_lan)
            kv.current = "train_with_brain"
            kv.transition.direction = "left"
        else:
            print('kniznica nema ziadne slovicka')


class WriteWindow(Screen):
    word = ObjectProperty(None)
    translated_word = ObjectProperty(None)
    # def btn(self):
    #     w =  Write.try_translate(self.word.text,to_lan,from_lan,board)
    #     if w == 1:
    #         self.translated_word.text = 'zadavas slovo v zlom jazyku'
    #     elif w == 0:
    #         self.translated_word.text = 'nemas internet'
    #     else:
    #         self.translated_word.text = w
    #     self.word.text = ""
    def btn(self):
        dict = {'type': 0,'to_tranlslate': [self.word.text]}
        self.trans(dict, to_lan = to_lan, from_lan = from_lan)

    def trans(self, *args, dict = {}, to_lan = '', from_lan = ''):
        
        url = "http://translate.pythonanywhere.com/t"

        # data = {"word":self.word.text, "to_lan":to_lan, "from_lan":from_lan}
        data = {"word":dict, "to_lan":to_lan, "from_lan":from_lan}
        headers = {'Content-type': 'application/json','Accept': 'text/plain'}

        self.r = UrlRequest(url, req_body=json.dumps(data), req_headers=headers,on_success=self.get_success ,on_failure= self.fail, on_error=self.fail)
        
    def get_success(self, *args):
        translated_word = str(self.r.result["word"])
        if  translated_word == 'Error':
            print('zasla si slovo v zlom jazyku')
            self.translated_word.text = "zadavas slovo v zlom jazyku"
        else:
            self.translated_word.text = translated_word
            print(self.r.result)

            if not Write.check_word(self.word.text, board):
                Write.append(self.translated_word.text, self.word.text, board, to_lan)
            else:
                print('uz tu je')
        self.word.text = ''

    def fail(self, *args):
        print("f")
        print(self.r.result)
        Write.have_not_network(self.word.text, board, to_lan, from_lan)
        self.translated_word.text = 'nemas internet'
        self.word.text = ''

   

    def focus(self):
        self.word.focus = True

    def translate_untranslated(self):
        def delete():
            with open(un_js, 'w') as f:
                d = {}
                json.dump(d, f)

        # try:
        with open(un_js, 'r') as f:
            data = json.load(f)
            fl = data[board]
            
            for wordf in fl:
                to_lan = fl[wordf]['to_lan']
                from_lan = fl[wordf]['from_lan']
                self.trans(word=wordf, to_lan = to_lan, from_lan = from_lan)
            f.close()
        delete()

        # except Exception as f:
        #     print('neni co na prelozenie')




class TrainingWindows(Screen):
    @classmethod
    def next_word(cls):
        cls.index += 1

    def show(self, cls):
        self.question.text = Training.different_langs(cls.words[cls.index], board, to_lan)

    def show_right_answer(self, ans):
        self.accuracy.text = str(self.question.text) + " = " +  str(ans)

    def answering(self, cls):
        # answer = self.answer.text.strip()
        answer  = self.answer.text

        # question = different_langs(cls.words[cls.index], board)
        ans = Training.check(cls.words[cls.index - 1] ,answer, board, to_lan)
        if ans == 1:
            self.accuracy.text = 'spravne'
            cls.correct += 1
            # self.uptade_right_answers(question, board)
        else:
            self.show_right_answer(ans)
        self.answer.text = ""

    def train(self, cls):

        cls = eval(cls)
        if cls.index == len(cls.words):
            self.answering(cls)
            #self.accuracy.text = "spravne " + str(TrainWindow.correct) + ' z ' + str(len(TrainWindow.random_numbers))
        elif cls.index > len(cls.words):
            self.accuracy.text = "spravne " + str(cls.correct) + ' z ' + str(len(cls.words))
        elif cls.index == 0:
            self.show(cls)
        else:
            self.answering(cls)
            self.show(cls)

    def focus(self):
        self.answer.focus = True

    def delete(self, cls):
        cls = eval(cls)
        cls.index = 0
        self.question.text = ''
        self.answer.text = ''
        cls.correct = 0
        #TrainWindow.random_numbers = Training.choose(board)
        self.accuracy.text = ''
    # def uptade_right_answers(self, question, board):
    #     with open(js, 'r') as f:
    #         data = json.load(f)
    #         fl = data[board]
    #         fl[question]['right_answers'] += 1
    #         json.dump(data, f, indent= 2)

class TrainWindow(TrainingWindows):

    question = ObjectProperty(None)
    accuracy = ObjectProperty(None)
    answer = ObjectProperty(None)
    index = 0
    correct = 0
    # def __init__(self, **kw):
    #     super().__init__(**kw)

class Train_with_brain_window(TrainingWindows):
    question = ObjectProperty(None)
    accuracy = ObjectProperty(None)
    answer = ObjectProperty(None)
    index = 0
    correct = 0
    # def __init__(self, **kw):
    #     super().__init__(**kw)
class Append_window(Screen):
    to_append = ObjectProperty(None)
    def append(self):
        string = self.to_append.text
        string = list(string)
        find  = False
        before = []
        after = []
        for letter in string:
            if find and letter == "=":
                after.append(letter)
            elif letter == "=":
                find = True
            elif find:
                after.append(letter)
            else:
                before.append(letter)
        if before[len(before)- 1] == " ":
            del before[len(before)- 1]
        if after[0] == " ":
            del after[0]
        
        before = ''.join(before)
        after = ''.join(after)
        with open(js, 'r+') as f:
            data = json.load(f)
            new = {before : {"translated": after, "right_answers": 0 }}
            data[board].update(new)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.close()
            

    def focus(self):
        self.to_append.focus = True
        print('fungujem')
class Manage_window(Screen):
    data = ObjectProperty(None)
    units = []
    index = 0
    def focus(self):
        self.data.focus = True
    def btn(self):
        print(self.data.text)
    def up(self):
        if Manage_window.index != 0:
            #Manage_window.units[Manage_window.index] = self.store_data(Manage_window.units[Manage_window.index])
            Manage_window.units[Manage_window.index] = self.data.text
            Manage_window.index -= 1
            self.fill()
    def down(self):
        
        if Manage_window.index + 1 < len(Manage_window.units):
            Manage_window.units[Manage_window.index] = self.data.text
            #Manage_window.units[Manage_window.index] = self.store_data(Manage_window.units[Manage_window.index])
            Manage_window.index += 1
            self.fill()
        
    def fill(self):
        self.data.text = Manage_window.units[Manage_window.index]
    def create_data(self):
        unit = 12
        to_fill = ''
        with open(js, 'r') as f:
            data = json.load(f)
            fl = data[board]
            
            c = 0
            for word in fl:

                
                
                if c < unit:
                    
                    to_fill = to_fill +  word  + '=' + fl[word]['translated'] + ',' + str(fl[word]['right_answers']) +  '\n'
                else:
    
                    Manage_window.units.append(to_fill)
                    
                    to_fill = ""
                    to_fill = to_fill +  word  + '=' + fl[word]['translated'] + '\n'
                    
                    c = 0
                    
                c += 1
            if to_fill != "":
                Manage_window.units.append(to_fill)
        self.fill()
        f.close()
    def store_data(self):
        Manage_window.units[Manage_window.index] = self.data.text
        final_string = ''
        for string in Manage_window.units:
            final_string = final_string + string
        
        find  = False
        find_comma = False
        before = []
        after = []
        rigt_answers = ''
        dict = {}
        for letter in final_string:
            if letter == "\n":
                
                before = ''.join(before)
                after = ''.join(after)

                dict[before] = {}
                dict[before]['translated'] = after
                try:
                    dict[before]['right_answers'] = int(rigt_answers)
                except:
                    print('nezadal si cislo')
                    dict[before]['right_answers'] = 0
                before = []
                after = []
                find = False
                find_comma = False
                rigt_answers = ""
            elif find and letter == "=":
                after.append(letter)
            elif letter == "=":
                find = True
            elif letter == ",":
                find_comma = True
            elif find_comma:
                rigt_answers = rigt_answers + letter
                
            elif find:
                after.append(letter)
            
            else:
                before.append(letter)
        print(dict)
        
        
        read = open(js, 'r')
        data = json.load(read)
        data[board] = dict    
        write = open(js, 'w')
        json.dump(data, write, indent=2)
        read.close()
        write.close()

    def delete(self):
        Manage_window.units = []
        Manage_window.index = 0

class WindowManager(ScreenManager):
    pass




kv = Builder.load_file("anj.kv")

class Anj(App):
    def build(self):
        return kv
if __name__ == "__main__":

    Anj().run()
