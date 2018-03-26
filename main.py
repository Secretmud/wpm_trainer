from time import time
import csv
import os



words_easy = ["ape", "ananas", "penger", "test", "kanskje", 
              "hvorfor", "hvordan", "hvor", "fordi", "tvilsomt", 
              "adekvat", "skildring", "minister", "Kvakksalver",
              "pendulum"]
words_medium = ["kvakksalver", "Minst", "Konsentrasjon",
                "Oppbygd", "Hostesaft", "Appelsinmarmelade"]
words_hard = ["TuLlBaLL", "AppLikaSJon", "OrdenTLIg", "AvKobbLInG"]
words_extreme = [";:/=+2$", "£€?/.#~]}", "!`\|@#~~#?-)", "^5*&$Hei"]
while __name__ == "__main__":
    max_score = 0
    correct = []
    wrong = []
    start_time = time()
    os.system('clear' or 'cls')
    print("This game will test your typing skills")
    print("There are 4 levels to try:\n" +
          "\t1. Easy\n" +
          "\t2. Medium\n" +
          "\t3. Hard\n" +
          "\t4. Extreme\n\n")
    difficulty = input("Choose your difficulty:")
    words = []
    if difficulty == "1":
        words.extend(words_easy)
        max_score = len(words_easy)
        os.system('clear' or 'cls')
        running = True
    elif difficulty == "2":
        words.extend(words_medium)
        max_score = len(words_medium)
        os.system('clear' or 'cls')
        running = True
    elif difficulty == "3":
        words.extend(words_hard)
        max_score = len(words_hard)
        os.system('clear' or 'cls')
        running = True
    elif difficulty == "4":
        words.extend(words_extreme)
        max_score = len(words_extreme)
        os.system('clear' or 'cls')
        running = True
    elif difficulty == "exit":
        print("Thanks for playing!")
        __name__ == "__spain__"
    
    while running:
        for i in words:
            print(i)
            answer = input("")
            print(words)
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
                x = len(correct)/(tot_time/60)
                print("that score would be equal to", x, "WPM")
                print("Time:", tot_time)
                print(correct)
                print(wrong)
                x = input("Press Enter to contiue")
                running = False
