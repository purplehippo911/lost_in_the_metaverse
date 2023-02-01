import time
import random

# main function
def start_chapter_2():
    # start of the chapter
    print("\n")
    print("______________________")
    print("Chapter 2 -- In school")
    print("______________________")


    # introduction
    print("\n Eileen is one of the quieter students in class, preferring to keep to herself and avoid conflict.")
    time.sleep(7)
    print("\n However, she finds herself in a difficult situation when a group of bullies enters the room, led by a particularly cruel student who starts picking on another student. Eileen watches as the other students back away, afraid to get involved.")
    time.sleep(9)
    print("\n Just as the situation seems to be escalating, Eileen steps in, using her words to try and diffuse the situation. Although the bully tries to tough it out, they eventually back down and challenge Eileen to a fight behind the basketball hoop after school.")
    time.sleep(9)    
    # choices

    ## second choice
    second_choice = input(" \n As school ends, Eileen is faced with a tough decision. Should she fight the bully, or should she run home and avoid the confrontation? Eileen thinks about her options and decides what she feels is best for her. Choose to either FIGHT or RUN: ")
    
    ### consequences of the first choice
    second_dice = random.randint(0,1)
    
    ### consequences of choosing fight
    fight_good_consequence = "Eileen decides to fight the bully, she faces a difficult challenge but remains steadfast in her beliefs. The fight takes place behind the basketball hoop after school, and although it is a difficult and tense situation, Eileen manages to come out on top. The bully and their gang leave with a newfound respect for Eileen, and she feels proud of herself for standing up for what was right."
    fight_bad_consequence = "Eileen decides to fight the bully, she soon realizes that this was not the best decision. Although she initially comes out on top, the bully retaliates by spreading rumors and false information about her, causing her to become an outcast at school. Eileen struggles to maintain her friendships and is constantly teased and bullied by other students. She regrets her decision to fight the bully and wishes she had taken a different approach."

    ### consequences of choosing run
    run_good_consequence = "Eileen decides to run home, she avoids the confrontation and stays safe, but she is left feeling guilty for not standing up for what was right. She spends the afternoon at home, thinking about the choices she has made and the bravery she could have shown."
    run_bad_consequence = "Eileen decides to run home, she avoids the confrontation, but the bully sees it as a sign of weakness. They and their gang continue to bully and harass other students, causing chaos and disruption in the school. Eileen is left feeling guilty for not standing up to the bully and wishes she had done more to help her fellow students. The situation at school only gets worse, and Eileen finds it increasingly difficult to focus on her studies."


    ## checking the first choice
    if second_choice.lower() == "fight":
        print("You chose to 'fight' \n")
        time.sleep(5)

        ## checking what consequence the user got
        if second_choice == 0:
            print(fight_good_consequence)
        else:
            print(fight_bad_consequence)
        time.sleep(9)
    else:
        print("You chose to 'run.' away(or rather avoid) \n")
        time.sleep(5)

        ## checking what consequence the user got
        if second_dice == 0:
            print(run_good_consequence)
        else:
            print(run_bad_consequence)
        time.sleep(9)
    