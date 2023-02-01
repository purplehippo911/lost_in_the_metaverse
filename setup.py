from setuptools import setup
import os

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='lost_in_the_metaverse_purplehippo911',
    scripts=[
        'main.py',
    ],
    version='0.0.1',
    description="A small RPG game run in the terminal",
    long_description="A RPG game made in Python about a girl attempting to escape her normal life and getting trapped in the metaverse.“As Eileen puts on the VR set, she is transported to a futuristic metaverse, where she is free to explore and experience new things. She falls into a virtual world, where she discovers she has the ability to create, explore, and manipulate her surroundings.However, her newfound freedom is short-lived, as she soon realizes that she is being pursued by an unknown entity. The robotic voice continues to ask her questions, and Eileen realizes that she has stumbled into a dangerous and unknown world.She tries to escape and find her way back to reality, but she is constantly pursued by the mysterious entity. Eileen must use her wits and her newfound abilities to evade her pursuer and find a way back to the real world. As she races against time, Eileen finds that the line between reality and virtual reality becomes blurred, and she must make choices that will determine her fate and the fate of those around her. Will she be able to find her way back to reality, or will she be trapped in the metaverse forever?'",
    author='Purplehippo911 (https://github.com/purplehippo911)',
    author_email='oceanrabbit0101@protonmail.com',
    url='https://github.com/purplehippo911/lost_in_the_metaverse',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: RPG Game",
        "Topic :: Adventure Game",
    ],
)