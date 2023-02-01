# some important modules
import time
import random

# main function
def start_chapter_3():
    # start of the chapter
    print("\n")
    print("--------------------")
    print("Chapter 3 -- Afternoon".upper())
    print("----------------------")

    # introduction
    print("\n One afternoon, Eileen goes straight to her room without talking to her family or eating dinner. She was feeling a little frustrated as she trudged up the stairs. Before sleeping, yesterday, she had the chance to get her hands on the mysterious package she had been expecting. With a sigh, she finally arrived at her bedroom and closed the door behind her.")
    time.sleep(9)
    print("\n Upon opening the package, Eileen was surprised to find cutting-edge metaverse or future-generation virtual reality gear inside. She felt an overwhelming urge to try it on right away, but at the same time, her mother's voice echoed up the stairs, demanding that she come down and have dinner with the rest of the family. ")
    time.sleep(9)
    print("\n If she put it on now, she would be able to get a taste of the virtual world, but it could also cause her to miss out on whatever her mother had planned for dinner. On the other hand, if she didn't put it on now, she could join her family for dinner and find out what her mother wanted, but also miss out on the chance to explore the virtual world.")
    time.sleep(9)    
    
    # choices

    ## third choice
    third_choice = input(" \n Eileen had a dilemma on her hands - should she put on the set and give in to her curiosity, or should she wait and see what her mother wanted? Choose to either START or WAIT: ")
    
    ### consequences of the first choice
    third_dice = random.randint(0,1)
    
    ### consequences of choosing start
    start_consequence = "Eileen felt a sudden rush of energy as she put on her glasses and headset, pressing the start button with trembling hands. She was determined to find out what was inside the mysterious package, despite the warnings of her mother. The air around her felt electric as her physical body fell to the ground, and Eileen found herself in a strange and unfamiliar place. She heard a robotic voice asking for her name and, without hesitation, she answered with a boldness she hadn't known she possessed. “Goldilocks, Leena Goldilocks,” she declared. Everything around her faded to black."

    ### consequences of choosing wait
    wait_consequence = "After some consideration, she decides to wait and see what her mother wanted. She opened her door, stepped out of her room, and called out to her mother that she would join them for dinner shortly. Once dinner was finished, Eileen hurried back to her room, eager to explore the unknown package, but she found out that the package was nowhere to be seen. \n"
    wait_consequence_2 = "It was a difficult situation for Eileen, who had been excited to use her new virtual reality headset. She had saved up her money for weeks, and was looking forward to exploring this new technology. However, her mother had other plans. With a stern warning, she confiscated the package, saying that it would not be tolerated while her daughter was in school. The disappointment was palpable, but Eileen knew she could not argue with her mother.\n"
    wait_consequence_3 = "Her week was filled with anxiety as she faced rumours and bullying at school. Her peers made her feel terrible, but she kept her head up and stayed strong. \n"
    wait_consequence_4 = "Finally, the day arrived when she was allowed to use the headset. She rushed home and went straight to her room, eager to explore the virtual world. She inserted the device and put on the special glasses, excited to see what awaited her. The experience was quite exhilarating, as she explored different landscapes, interacted with characters and objects, and even visited places she had never been before. After hours of exploration, she removed the headset, feeling refreshed and energized. \n"
    wait_consequence_5 = "Eileen smiled to herself, proud of her accomplishment and thankful that her mother allowed her to use the headset, even if it meant waiting a whole week. She was now more determined than ever to prove her mother's trust was not misplaced.\n"
    wait_consequence_6 = "One weekend, while trying the VR on she experienced something new. There was said to be a major update due tonight. After finishing the installation of the update, Eileen takes it on and she hears the robotic voice asking for her name and, without hesitation, she answered with a boldness he hadn't known she possessed. “Goldilocks, Leena Goldilocks,” she declared. 'Hi, Goldilocks', says the robotic voice. 'Hope you enjoy the new update'. \n"
    wait_consequence_7 = "After a night of playing, Eileen felt exausted. She was trying to take a break for today, but as she went to click the logout button, she noticed it had disappeared. A robotic voice suddenly came from nowhere, informing her that she wouldn't be able to leave for a certain amount of time. She was horrified at the thought of being trapped in the virtual world, with no way of getting out. As the minutes passed, she began to panic, uncertain of what would happen next. Would she ever be able to escape? What would happen if she couldn't? These questions kept running through her head, as the robotic voice echoed in the distance. There was a bug in the system. Everything around her faded to black. \n"

    ## checking the first choice
    if third_choice.lower() == "start":
        print("You chose to 'start' \n")
        time.sleep(5)

        print(start_consequence)
        time.sleep(9)
    else:
        print("You chose to 'wait.' \n")
        time.sleep(5)

        print(wait_consequence)
        time.sleep(9)

        print(wait_consequence_2)
        time.sleep(9)

        print(wait_consequence_3)
        time.sleep(9)

        print(wait_consequence_4)
        time.sleep(9)

        print(wait_consequence_5)
        time.sleep(9)

        print(wait_consequence_6)
        time.sleep(9)

        print(wait_consequence_7)
        time.sleep(9)