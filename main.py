from time import time
import wikipedia
import os
from random import randint
import threading

class colors:
    right = '\033[92m'
    wrong = '\033[91m'
    endc = '\033[0m'

search = ["Donald Knuth", "Brian Kernighan", "Dennis Richie", "Richard Stallman", "Linus Torvalds"]

def game(word, difficulty):
    correct = []
    wrong = []
    start_time = time()
    words = wikipedia.summary(word, sentences=difficulty)
    word_list = []
    word_list.extend(words.split())

    if (len(correct)+len(wrong))< len(word_list):
        for i in word_list:
            word_len_ans = ((len(correct)) + (len(wrong)))
            os.system('clear' or 'cls')
            strings = ' '.join(word_list)
            print(strings)
            ttime = (int(time() - start_time))
            print(ttime)
            print(word_len_ans, "/", len(word_list))
            test = input()
            ind_place = word_list.index(i)
            if test in strings:
                x = (colors.right + i + colors.endc)
            if test not in word_list:
                y = (colors.wrong + i + colors.endc)
            if test in word_list:
                word_list.insert(ind_place, x)
                word_list.remove(i)
                correct.append(test)
            elif test not in word_list:
                word_list.insert(ind_place, y)
                word_list.remove(i)
                wrong.append(test)

    if (len(correct)+len(wrong)) == len(word_list):

        os.system('clear' or 'cls')
        points = (len(correct)-len(wrong))
        percentage_correct = ((len(correct)/len(word_list)*100))
        key_c = sum(len(i) for i in correct)
        key_w = sum(len(i) for i in wrong)
        key_t = key_c + key_w
        wpm = ((key_t/(ttime*0.0166667))
        max_points = len(word_list)

        print("Score board:\nPoints: {0}/{1}\nPercentage correct {4}%\nWPM: {2}\nTime: {3}\n".format(points, max_points, wpm, ttime, percentage_correct))
        
        exit = input()

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
        game(search[rand_search], 2)
    if diff == "2":
        game(search[rand_search], 5)
    if diff == "3":
        game(search[rand_search], 7)
    if diff == "4":
        game(search[rand_search], 9)
