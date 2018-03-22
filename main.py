from time import time
from random import randrange
import csv
import os
words = ["ape", "ananas", "penger", "test", "kanskje", 
         "hvorfor", "hvordan", "hvor", "fordi", "tvilsomt", 
         "adekvat", "skildring", "minister"]
max_score = len(words)
correct = []
wrong = []

os.system('clear' or 'cls')
print("This game will test your typing skills")

pick = randrange(0, len(words))

start_time = time()
end = time() + 10
running = True


while running:
    for i in words:
        if end > start_time:
            print(i)
            answer = input("")
            if answer == i:
                correct.append(i)
                words.remove(i)
            elif answer != i:
                wrong.append(i)
                words.remove(i)
             
            os.system('clear' or 'cls')
        if len(words) == 0:
            tot_time = time() - start_time
            print("You made it with:")
            print(str(len(correct)) + "/" + str(max_score))
            x = (len(correct)*60)/tot_time
            print("that score would be equal to", x, "WPM")
            print("Time:", tot_time)
            running = False
