# main file -- here's where most of my functions run

## for making breaks inbetween texts, by using time.sleep()
import time

## importing the start functions from the chapters and turtle drawing
from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3
from drawing import start_drawing

## start the drawing function
start_drawing()
time.sleep(5)


## here's where the game runs, by checking if the chapter functions actually exists
while [start_chapter_1, start_chapter_2, start_chapter_3]:
    ### Game Title
    print("----------------------")
    print("Stuck in the metaverse".upper())
    print("---------------------- \n")
    time.sleep(3)

    ### running the chapters
    start_chapter_1()
    time.sleep(5)

    start_chapter_2()
    time.sleep(5)

    start_chapter_3()
    time.sleep(5)


    ### credits
    print("_________________________________________")
    print("\n Developer: 'Purplehippo911' / Omer \n")
    time.sleep(3)
    print("Story made with help by both ChatGPT-3 by OpenAI and ChatSonic by WriteSonic.")
    print("_________________________________________")