from time import time
import wikipedia
import os
from random import randint
import threading



search = ["Donald Knuth", "Brian Kernighan", "Dennis Richie", "Richard Stallman", "Linus Torvalds"]

def game(word, difficulty):
    start_time = time()
    correct = []
    wrong = []
    word_list = []
    words = wikipedia.summary(word, sentences=difficulty)
    word_list.extend(words.split())
    points = (len(correct) - len(wrong))
    if (len(correct)+len(wrong))< len(word_list):
        for i in word_list:
            print(pressed)
            word_len_ans = ((len(correct)) + (len(wrong)))
            os.system('clear' or 'cls')
            strings = ' '.join(word_list)
            print(strings)
            ttime = (int(time() - start_time))
            print(ttime)
            print(word_len_ans, "/", len(word_list))
            test = input()
            if test in word_list:
                correct.append(test)
            else:
                wrong.append(test)
    if (len(correct)+len(wrong))>= len(word_list):
        os.system('clear' or 'cls')
        percentage_correct = ((len(correct)/len(word_list)*100))
        wpm = ((len(words)/int(ttime))*int(percentage_correct))
        max_points = len(word_list)
        print("Score board:\nPoints: {0}/{1}\nWPM: {2}\nTime: {3}\n".format(points, max_points, wpm, ttime))
        exit = input()
        if exit == "Yes":
            threading.stop()

while __name__ == "__main__":
    rand_search = randint(0, len(search) -1)
    os.system('clear' or 'cls')
    print("This is the menu\n" +
          "\t1. Easy\n" +
          "\t2. Medium\n" +
          "\t3. Hard\n" +
          "\t4. Extreme\n\n")
    diff = input()
    if diff == "1":
        game(search[rand_search], 2))
    if diff == "2":
        game(search[rand_search], 5)
    if diff == "3":
        game(search[rand_search], 7)
    if diff == "4":
        game(search[rand_search], 9)
    






