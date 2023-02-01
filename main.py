# main file -- here's where most of my functions run

## for making breaks inbetween texts, by using time.sleep()
import time

## importing the start functions from the chapters and turtle drawing
from src.chapters.chapter_1 import start_chapter_1
from src.chapters.chapter_2 import start_chapter_2
from src.chapters.chapter_3 import start_chapter_3
from src.drawing import start_drawing

## start the drawing function
start_drawing()
time.sleep(1)


## here's where the game runs, by checking if the chapter functions actually exists
while [start_chapter_1, start_chapter_2, start_chapter_3]:
    ### Game Title
    print("----------------------")
    print("Stuck in the metaverse".upper())
    print("---------------------- \n")
    time.sleep(2)

    ### running the chapters
    start_chapter_1()
    time.sleep(3)

    start_chapter_2()
    time.sleep(3)

    start_chapter_3()
    time.sleep(3)


    ### credits
    time.sleep(5)
    print("_________________________________________")
    print("\n Developer: 'Purplehippo911' / Omer \n")
    time.sleep(2)
    print("Story made with help by both ChatGPT-3 by OpenAI and ChatSonic by WriteSonic.")
    print("_________________________________________")

    # retry the game
    retry = input("Do you want to play again? (write yes or no): ")

    if retry.lower() != "yes":
        print("Thanks for playing \n")
        print("__________________")
        break
    else:
        start_drawing()
        continue

