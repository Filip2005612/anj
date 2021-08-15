from nltk.util import choose
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

Write.create()
file = ""
to_lan = ""
from_lan = ""
#app classs

class AskWindow(Screen):
    f = ObjectProperty(None)
    to = ObjectProperty(None)
    from_lan = ObjectProperty(None)

    def btn(self):
        global file, to_lan, from_lan
        file = self.f.text
        to_lan = self.to.text
        from_lan = self.from_lan.text

     
     

class ModeWindow(Screen):
    def new_file(self):
        print('vytvaram novu filu')
        Write.new_file(file)
        TrainWindow.random_numbers = Training.choose(file)

        
        

        




class WriteWindow(Screen):
    word = ObjectProperty(None)
    translated_word = ObjectProperty(None)
    def btn(self):
        
        self.translated_word.text = Write.translate(self.word.text,to_lan,from_lan,file)
        self.word.text = ""

class TrainWindow(Screen):
    
    question = ObjectProperty(None)
    accuracy = ObjectProperty(None)
    answer = ObjectProperty(None)
   
    
    index = 0
    correct = 0
    def __init__(self, **kw):
        super().__init__(**kw)

    def show(self):
        self.question.text = Training.train(file,TrainWindow.random_numbers, TrainWindow.index, to_lan)
        TrainWindow.index += 1
        

    def answering(self):
        
        answer = self.answer.text.strip()
        ans = Training.check(TrainWindow.index,TrainWindow.random_numbers, answer, file, to_lan)
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
        TrainWindow.random_numbers = Training.choose(file)
        self.accuracy.text = ''
    



class WindowManager(ScreenManager):
    pass






kv = Builder.load_file("anj.kv")

class Anj(App):
    def build(self):
        return kv
if __name__ == "__main__":
    
    Anj().run()
