import time

#importing the start functions from the chapters
from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3


# Game Title
print("----------------------")
print("Stuck in the metaverse".upper())
print("---------------------- \n")
time.sleep(1)

# running the chapters
start_chapter_1()
time.sleep(3)

start_chapter_2()
time.sleep(3)

start_chapter_3()
time.sleep(3)


# credits
print("_________________________________________")
print("\n Developer: 'Purplehippo911' / Omer \n")
time.sleep(3)
print("Story made with help by both ChatGPT-3 by OpenAI and ChatSonic by WriteSonic.")
print("_________________________________________")
