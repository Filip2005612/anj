from re import S
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from nltk import text
from textblob import TextBlob
import json




#app classs

class ModeWindow(Screen):
    pass

class AskWindow(Screen):
    
    file = ObjectProperty(None)
    to = ObjectProperty(None)
    from_lan = ObjectProperty(None)

    
    def btn(self):
        WriteWindow.file = self.file.text
        WriteWindow.to_lan = self.to.text
        WriteWindow.from_lan = self.from_lan.text
        WriteWindow().create()



class WriteWindow(Screen):
    word = ObjectProperty(None)
    def btn(self):
        self.translate(self.word.text,WriteWindow.to_lan, WriteWindow.from_lan)
        
        self.word.text = ""
        
    def translate(self, word_to_trans, to_lan, from_lan):
        #print(to_lan)
         
        word = str(TextBlob(word_to_trans).translate(to = to_lan, from_lang= from_lan))
        # print(word)
        if not self.check_word(word):
            self.append(word, word_to_trans)

    def append(self, word, text):
        file = WriteWindow.file
        language = WriteWindow.to_lan
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


    def check_word(self, word):
        file = WriteWindow.file
        f = open('data/global.json')
        data = json.load(f)
        #print(file)
        fi = data[file]

        for key in fi:
            if key == word:
                print('uz tu je')
                return True
            if fi[key] == word:
                print('uz tu je')
                return True
        return False


    def create(self):
        file = WriteWindow.file
        try:
            
            f = open('data/global.json', 'r+')
            
            
            data = json.load(f)
            try:
                
                a = data[file]
            except:
                
                fl = {file : {}}
                data.update(fl)
                f.seek(0)
                json.dump(data, f, indent=2)
            
        except:
            
            f = open('data/global.json', 'a')
            
            d = {file : {}}
            f.seek(0)
            json.dump(d, f, indent= 2)
        f.close()



  






class WindowManager(ScreenManager):
    pass



kv = Builder.load_file("anj.kv")

class Anj(App):
    def build(self):
        return kv
if __name__ == "__main__":
    
    Anj().run()



#app functions








  



    





