import os
import random

class WordList():  
    word_list = []
    def __init__(self): 
        list = self.__read_file()
        self.word_list = self.__split_list_in_words(list)

    def __split_list_in_words(self, list):
        word_list = []
        for line in list:
            res = line.split(';')
            word_list.append(res)
        return word_list

    def __read_file(self):
        try: 
            file = open("woorden.txt", "r")
            list = []
            for line in file.readlines():
                if line.strip():
                    list.append(line.rstrip())
            file.close()
        except:
            return "niet gelukt"
        return list

    def get_word_list(self): 
        return self.word_list   

class WordGame():
    max_words = 0
    wordlist = []
    def __init__(self):
        _wordlist = WordList()
        self.wordlist = _wordlist.get_word_list()
        self.max_words = len(self.wordlist)

    def __get_word(self): 
        random.shuffle(self.wordlist)
        return self.wordlist[0]

    def print_explanation(self): 
        os.system('cls' if os.name=='nt' else 'clear')
        print("**********************************************************************")
        print("* Welcome at the Englisch word game. This game will teach you the    *")
        print("* irregular verbs. good luck                                         *")
        print("**********************************************************************")

    def play(self): 
        self.print_explanation()
        while (len(self.wordlist) > 0): 
            play_word = self.__get_word()
            word = input("({})  ==> {} ({}): ".format(str(len(self.wordlist)),play_word[0], play_word[3]))
            if word.lower() ==play_word[1].lower(): 
                del self.wordlist[0]
            else:
                print("Nope: that is {}".format(play_word[1]))

g = WordGame()
g.play() 