from textblob import TextBlob
from collections import OrderedDict
import random
import json
import socket
from textblob.blob import Word
from kivy.app import App
from kivy.uix.widget import Widget
print('Zadaj w ked chces pridavat nove slovicka alebo zadaj t ked chces precvicovat a ked chces skoncit progarm zadaj q' + '\n')

# file = input('zadaj stranku: ')
# mode = input('Zadaj mĂłd: ')
# language = input('preloz do jazyka: ')
# from_language = input('preloz z jazyka: ')


# # file = 'kniha'
# # mode = 'w'
# # language = 'en'
# # from_language = 'sk' 

# run = True




# def new_file(open):
#     data = json.load(open)
    
#     try:
#         a = data[file]
#     except:
#         fl = {file : {}}
#         data.update(fl)
#         open.seek(0)
#         json.dump(data, open, indent=2)


        


        
    
        
# def create():
#     try:
#         f = open('data/global.json', 'r+')
#         new_file(f)
#         f.close()
#     except:
#         f = open('data/global.json', 'a')
#         d = {file : {}}
#         json.dump(d, f, indent= 2)
#         f.close()


# create()

# def append(word, text):
#     with open('data/global.json', 'r+') as f:
        
#         if language != 'sk':
#             new = {word : text}
#             data = json.load(f)
#             data[file].update(new)
#             f.seek(0)
#             json.dump(data, f, indent=2)
#             f.close()
            
#         else:
#             new = {text : word}
#             data = json.load(f)
#             data[file].update(new)
#             f.seek(0)
#             json.dump(data, f, indent=2)
#             f.close()

    


# def check_word(word):
#     f = open('data/global.json')
#     data = json.load(f)
    
#     fi = data[file]

#     for key in fi:
#         if key == word:
#             print('uz tu je')
#             return True
#         if fi[key] == word:
#             print('uz tu je')
#             return True
#     return False 

# def translate():
    
#     word = str(TextBlob(text).translate(to = language, from_lang= from_language))
#     print(word)
#     if not check_word(word):
#         append(word, text)
    
    








# def alphabetcally(file):
#     with open('data/global.json', 'r+') as f:
#         data = json.load(f)
#         fl = data[file]
#         sor = sorted(fl.items(), key = lambda t: t[0])
#         json.dump(sor, f , indent=2)

#         # data = json.load(f)
#         # fl = data[file]
#         # sort = OrderedDict(sorted(fl.items()))
#         # dic = {}
#         # for i in sort:
#         #     dic[i] = fl[i]
#         # json.dump(dic, fl, indent=2)
            



# def answer(i, lines):
#     command = 'c'
#     if language == 'sk':
#         word = lines[i][0]
#         right_answer = lines[i][1]
#         answer = input(word + ': ')
#         if answer == 'c':
            
#             return command
#         else:
#             if answer == right_answer:
#                 print('spravne')
#                 return True
#             else:
#                 print('nespravne malo to byt: ' + right_answer)
#                 return False
#     if language == 'en':
#         word = lines[i][1]
#         right_answer = lines[i][0]
#         answer = input(word + ': ')
#         if answer == 'c':
#             return command
#         else:
#             if answer == right_answer:
#                 print('spravne')
#                 return True
#             else:
#                 print('nespravne malo to byt: ' + right_answer)
#                 return False
# def next():
#     global run
#     next = input('Chces dalej pokracovat?: A/N/c ')
#     if next.upper() == 'N':
#         run = False
#     if next.upper() == 'A':
#         train()
#     if next.upper() == 'C':
#         commands()

# def train():
#     correct = 0
#     with open('data/global.json', 'r') as f:
#         data = json.load(f)
        
#         lines = list(data[file].items())

#         try:
#             random_numbers = random.sample(range(len(lines)), 10)
#         except:
#             random_numbers = random.sample(range(len(lines)), len(lines))
#         for index in random_numbers:
#             ans = answer(index, lines)
#             if ans == 'c':
#                 c = commands()
#                 if c == 'w' or c == 'q':
#                     return
#             else:

#                 if ans:
#                     correct += 1
            
            
            
            

#         print('spravne: ' + str(correct) + ' z ' + str(len(random_numbers)))
#         f.close()
    
            
#     next()
# def backup(word):
#     with open('data/backup.txt', 'a') as f:
#         f.write(word + '\n')
#         f.close()
# def commands():
#     global run, mode, file
#     print('mozes zadavat comandy')
#     command = input('sem: ')
#     if command == 'q':
#         run = False
#         return 'q'
#     if command == 't':
#         mode = 't'
        
#     if command == 'w':
#         mode = 'w'
#         return 'w'
#     if command  == "FILIP JE NOOB":
#         print('nemas pravdu')
#     if command == 'file':
#         f = input('zadaj inu stranku: ')
#         file = f
#         return 'q'
#     return



# def have_not_network(word):
#     f = open('data/untranslated.txt', 'a')
#     f.write(word + '\n')
#     f.close()


# def translate_untranslated():

#     with open('data/untranslated.txt', 'r') as f:
#         text = f.read()

#         text = text.strip()
#         text = text.split()
#         def delete():
#             with open('data/untranslated.txt', 'w') as fl:
#                 fl.write('')
#                 fl.close()
#         for i in text:
#             if not check_word(i):
#                 try:
#                     w = str(TextBlob(i).translate(to = language, from_lang= from_language))
#                     append(w, i)
#                     print(w)
#                 except:
#                     w = str(TextBlob(i).translate(to = from_language, from_lang= language))
                    
#                     append(i, w)
#                     print(w)
#         f.close()
#     delete()
                

# while run:
#     if mode.upper() == 'W':
        
#         text = input('Zadaj slovo debile: ')
#         if text == 'c':
#             commands()
#         else:
            
#             IPaddress = socket. gethostbyname(socket. gethostname())
#             try:
#                 backup(text)
#                 translate()
#                 translate_untranslated()
                
#             except :
                
#                 if IPaddress =="127.0.0.1":
#                     print('nemas internet debil')
#                     have_not_network(text)
            
#                 else:
#                     print('zadavas slovo v zlom jazyku')

        

#     if mode.upper() == 'T':
#         train()
        

# #alphabetcally(file)
# #alphabetcally('global.txt')
# print('koniec')







class MyGrid(Widget):
    def pressed(self, instance):
        word = 
        last = self.last_name.text
        email = self.email.text

        print('name:', name, last, email)
        self.name.text = ""
        self.last_name.text = ''
        self.email.text = ''

class grid(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    grid().run()