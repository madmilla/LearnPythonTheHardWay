import random
from urllib.request import urlopen
import system

WORD_URL = "http://learncodethehardway.com/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(Object): \n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** parameters",
    "class %%%(object): \n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ paramter",
    "*** = %%%(@@@)":
        "Set *** to an instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'"
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readline():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [x.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sampe(WORDS, snippet.count("***"))
    result = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
