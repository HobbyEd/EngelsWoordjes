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
            file = open("korte_woordenlijst.txt", "r")
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
    wordlist = []
    def __get_word(self): 
        random.shuffle(self.wordlist)
        return self.wordlist[0]

    def print_explanation(self): 
        os.system('cls' if os.name=='nt' else 'clear')
        print("**********************************************************************")
        print("* Welcome at the Englisch word game. This game will teach you the    *")
        print("* irregular verbs. Enter both the past and the past participle       *")
        print("* seperated by space. Good luck!!                                    *")
        print("**********************************************************************")

    def play(self): 
        keep_playing = True
        while keep_playing:
            wordlist = WordList()
            self.wordlist = wordlist.get_word_list()    
            self.print_explanation()
            while (len(self.wordlist) > 0): 
                play_word = self.__get_word()
                answer = input("({})  ==> {} ({}): ".format(str(len(self.wordlist)),play_word[0], play_word[3]))
                answerlist = answer.split(" ")
                if len(answerlist) == 2: #check whether two words have been entered 
                    past = answerlist[0] 
                    past_participle = answerlist[1]
                    if (past.lower() == play_word[1].lower()) and (past_participle.lower() == play_word[2].lower()): 
                        del self.wordlist[0]
                    else:
                        print("Nope: past is \033[92m{}\033[0m and past participle is \033[92m{}\033[0m".format(play_word[1], play_word[2]))
                else:
                    print("Enter both the past and the past participle seperated by space.")
            again = input("Nice!! that were al the words. Shall we do it again (Y)?")
            if not (again.lower() == "y"): 
                keep_playing = False

g = WordGame()
g.play() 
