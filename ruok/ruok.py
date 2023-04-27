# Required
# pip3 install -q transformers
# pip3 install tensorflow

import os
import sys
import random
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TRANSFORMERS_VERBOSITY'] = 'critical'
from transformers import pipeline

# get data
commit_msg = sys.stdin.read()

sentiment_pipeline = pipeline(model="cardiffnlp/twitter-roberta-base-sentiment")
data = [commit_msg,]
stmt = sentiment_pipeline(data)

positive_titles = [
    "Fuck yeah!",
    "Awesome",
    "Proud of you",
    "Schwing!",
    "Killing it!",
    "Fairest of them all",
]

positive_messages = [
    "I hope I'm half as happy as you are!",
    "Excellent commit. 10/10. No notes.",
    "You're doing a great job.",
    "Your collaborators are real lucky to have you.",
    "Smooth as butter.",
    "Nothing but net.",
]

negative_titles = [
    "Woah there!",
    "Deep breaths",
    "You've got this",
    "A little annoyed?",
    "Perhaps a walk?",
]

negative_messages = [
    "Maybe get some fresh air -- you seem a little agitated.",
    "Picking up some tense vibes. Maybe time for a snack?",
    "Take five and text someone you care about!",
    "Don't let the code win. It's a smug bastard and it'll never let you hear the end of it!",
    "I suggest grabbing a drink of water and a little stretch.",
]

if stmt[0]["label"] == 'LABEL_0':
    # negative
    if stmt[0]["score"] > 0.60:
        os.system('notify-send "{}" "{}"'.format(random.choice(negative_titles), random.choice(negative_messages)))
elif stmt[0]["label"] == 'LABEL_2':
    if stmt[0]["score"] > 0.60:
        os.system('notify-send "{}" "{}"'.format(random.choice(positive_titles), random.choice(positive_messages)))
