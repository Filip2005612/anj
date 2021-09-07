import json

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import Write
import Training
import com
# import os
js = "data/global.json"
Write.create(js)
Write.create('data/untranslated.json')
board = ""
#testovaca verzia






to_lan = "sk"
from_lan = "en"




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
    def train(self):
        if not Training.check_file(board):
            print('idem trenovat')
            TrainWindow.words = Training.choose(board, to_lan)
            kv.current = "train" 
            kv.transition.direction = "left" 
        else:
            print('kniznica nema ziadne slovicka')

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
            with open('data/untranslated.json', 'w') as f:
                d = {}
                json.dump(d, f)

        try:
            with open('data/untranslated.json', 'r') as f:
                data = json.load(f)
                fl = data[board]
                
                for word in fl:
                    
                    trns = Write.try_translate(word, data[board][word]['to_lan'], data[board][word]['from_lan'], board)
                    if trns == 0:
                        print('nemas internet')
                        return
                    if trns == 1:
                        print('zadal si slovo v zlom jazyku')

                # data = {}
                # json.dump(data, f, indent=2)
                f.close()
            print('idem deletovat')
            delete()
        except Exception as f:
            print(f)
            print('neni co na prelozenie')


            
        
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

    
class WindowManager(ScreenManager):
    pass






kv = Builder.load_file("anj.kv")

class Anj(App):
    def build(self):
        return kv
if __name__ == "__main__":
    
    Anj().run()
