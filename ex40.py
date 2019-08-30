class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So i'll stop right here"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

test = ["Are you you? Are you me?",
"Or someone in between?",
"You lost track inside the labyrinth",
"You lost your will and your sanity",
"You certainly lost your humanity",
"In life, you have taken much more than you're worth",
"Now it's your turn to give back to the Earth",
"May you return to the ground and ossify",
"It's time for you to die, die, die"]

gizzard = Song(test)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
gizzard.sing_me_a_song()
