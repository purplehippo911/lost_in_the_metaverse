import time
import random

# main function
def start_chapter_1():
    
    # start of the chapter
    print("Chapter 1 -- Waking up")
    print("______________________")

    # introduction
    print("\n Eileen Goldthorpe, an Estonian teenage girl, was fast asleep after a long and hectic day. She had been running around, trying to balance school work and extracurricular activities, and was exhausted.")
    time.sleep(9)
    print("\n The next morning, she wakes up in a panic, realizing she overslept and will be late for school. Eileen rushes to get dressed, grabbing a quick breakfast on the way out the door. As she makes her way to the bus stop, she checks the time and realizes the bus is running late.")
    time.sleep(9)
    print("\n Eileen begins to feel the pressure of time as she waits for the bus, knowing that every minute counts. She starts to weigh her options and decides she can't afford to wait for the bus any longer. Just then, she remembers a shortcut that would take her directly to school.")
    time.sleep(9)

    # choices

    ## first choice
    first_choice = input(" \n With the weight of the decision on her shoulders, Eileen must choose: should she wait for the BUS and risk being late for school, or should she take the SHORTCUT and hope for the best? This choice will determine if she makes it to school on time and sets the tone for the rest of her day. Choose BUS or SHORTCUT: ")
    
    ### consequences of the first choice
    first_dice = random.randint(0,1)
    
    ### consequences of choosing bus
    bus_good_consequence = "Eileen decides to wait for the bus, she eventually arrives at school just in time for the first bell. She rushes to her locker, grabs her books, and rushes to class. Although she makes it to school on time, she is frazzled and stressed for the rest of the day, constantly worried about being late for her next class."
    bus_bad_consequence = "Eileen decides to wait for the bus, she ends up missing it and having to wait for the next one. The next bus takes even longer to arrive and by the time she finally reaches school, she is late for her first class. She is scolded by her teacher and given detention for being tardy. The rest of the day is spent trying to make up for the lost time and she is unable to focus on her studies, feeling overwhelmed and stressed."

    ### consequences of choosing shortcut
    shortcut_good_consequence = "Eileen decides to take the shortcut, she cuts through alleys and side streets, making her way to school as quickly as possible. Along the way, she encounters some obstacles and challenges, but she remains determined to make it to school on time. When she finally arrives at school, she is out of breath and a little disheveled, but she made it. The rest of her day goes smoothly, and she is proud of herself for taking control of the situation."
    shortcut_bad_consequence = "Eileen decides to take the shortcut, she quickly realizes that it was a mistake. She encounters a dangerous situation and is forced to turn back. She is even later for school now and her stress level rises with each passing minute. When she finally arrives at school, she is scolded by her teachers for being late and disruptive. The rest of the day is spent in detention and she misses important classwork. Eileen is filled with regret for not waiting for the bus and for not considering the consequences of her actions."


    ## checking the first choice
    if first_choice.lower() == "bus":
        print("You chose 'bus' \n")
        time.sleep(5)

        ## checking what consequence the user got
        if first_dice == 0:
            print(bus_good_consequence)
        else:
            print(bus_bad_consequence)
        time.sleep(9)
    else:
        print("You chose 'shortcut.' \n")
        time.sleep(5)

        ## checking what consequence the user got
        if first_dice == 0:
            print(shortcut_good_consequence)
        else:
            print(shortcut_bad_consequence)
        time.sleep(9)
    