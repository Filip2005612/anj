import json
from sys import path
from nltk.util import choose, pr
from logging import NOTSET
from re import I, S
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from nltk import text
from textblob import TextBlob
import Write
import Training
import com
import os
js = "data/global.json"
Write.create(js)
board = ""
to_lan = ""
from_lan = ""




#app classs
class NameWindow(Screen):
    name_of_user = ObjectProperty(None)
    def btn(self):
        pass
    def upload(self):
        with open('data/global.json', 'r') as f:
            data = json.load(f)
            data = json.dumps(data)
            com.upload('filip', data)
        print('upload')
    def delete(self):
        print('delete')
    def download(self):
        print('download')




class AskWindow(Screen):
    f = ObjectProperty(None)
    to = ObjectProperty(None)
    from_lan = ObjectProperty(None)

    def btn(self):
        global board, to_lan, from_lan
        board = self.f.text
        to_lan = self.to.text
        from_lan = self.from_lan.text
        
        if to_lan == '':
            print('nezadal si jazyk')
        elif from_lan == '':
            print('nezadal si jazyk')
        else:
            kv.current = "mode"
            kv.transition.direction = "left"
            #Write.alphabetcally(file)
            Write.new_file(js, board)

        
        
     

class ModeWindow(Screen):
    def btn(self):
        if not Training.check_file(board):
            print('idem trenovat')
            TrainWindow.random_numbers = Training.choose(board)
            kv.current = "train" 
            kv.transition.direction = "left" 
        else:
            print('kniznica nema ziadne slovicka')
    

        
        

        



class WriteWindow(Screen):
    word = ObjectProperty(None)
    translated_word = ObjectProperty(None)
    def btn(self):
        w =  Write.try_translate(self.word.text,to_lan,from_lan,board)
        if w == 1:
            self.translated_word.text = 'zadavas slovo v zlom jazyku'
        elif w == 0:
            self.translated_word.text = 'nemas internet'
        else:
            self.translated_word.text = w
        self.word.text = ""
    def focus(self):
        self.word.focus = True
    def translate_untranslated(self):
        def delete():
            path = "data/untranslated.json"
            if os.path.exists(path):
                os.remove(path)
            else:
                print('neni taka')
        try:
            with open('data/untranslated.json', 'r') as f:
                data = json.load(f)
                
                for board in data:
                    print(board)
                    for word in data[board]:
                        print(word)
                        try:
                            Write.translate(word, to_lan, from_lan, board)
                        except:
                            print('nemas internet')
                            return
                f.close()
            delete()
        except:
            print('neni co na prelozenie')


            
    
class TrainWindow(Screen):
    
    question = ObjectProperty(None)
    accuracy = ObjectProperty(None)
    answer = ObjectProperty(None)
   
    
    index = 0
    correct = 0
    def __init__(self, **kw):
        super().__init__(**kw)

    def show(self):
        self.question.text = Training.train(board,TrainWindow.random_numbers, TrainWindow.index, to_lan)
        TrainWindow.index += 1
        

    def answering(self):
        
        answer = self.answer.text.strip()
        ans = Training.check(TrainWindow.index,TrainWindow.random_numbers, answer, board, to_lan)
        if ans == 1:
            self.accuracy.text = 'spravne'
            TrainWindow.correct += 1
        else:
            self.accuracy.text = 'nespravne ' + str(ans)
        self.answer.text = ""

    def train(self):
        
        if TrainWindow.index >= len(TrainWindow.random_numbers):
            self.accuracy.text = "spravne " + str(TrainWindow.correct) + ' z ' + str(len(TrainWindow.random_numbers))
        else:
            self.answering()
            self.show()
    def focus(self):
        self.answer.focus = True
    def delete(self):
        TrainWindow.index = 0
        self.question.text = ''
        self.answer.text = ''
        TrainWindow.correct = 0
        TrainWindow.random_numbers = Training.choose(board)
        self.accuracy.text = ''




class WindowManager(ScreenManager):
    pass






kv = Builder.load_file("anj.kv")

class Anj(App):
    def build(self):
        return kv
if __name__ == "__main__":
    
    Anj().run()
