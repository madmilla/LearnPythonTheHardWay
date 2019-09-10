from sys import exit
from random import randint
from textwrap import dedent

"""
“Aliens have invaded a space ship and our hero has to go through a maze of
rooms defeating them so he can escape into an escape pod to the planet
below. The game will be more like a Zork or Adventure type game with text
outputs and funny ways to die. The game will involve an engine that runs a
map full of rooms or scenes. Each room will print its own description when
the player enters it and then tell the engine what room to run next out of the
map."""



class Scene(object):
    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        pass

    def play(self):
        current_scene = self.scene_map.opening_scene()
        final_scene = self.scene_map.next_scene("finished")

        while current_scene != final_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()
        # Game loop
        pass

class Death(Scene):
    # Death This is when the player dies and should be something funny.
    def enter(self):
        pass

class CentralCorridor(Scene):
    # This is the starting point and has a Gothon already
    # standing there that the players have to defeat with a joke before continuing.
    def enter(self):
        print("looking around you see a couple doors and a sign: [Central Corridor] ")
        if (TheBridge.power_on == False & TheBridge.alarm_off):
            print("It's pitch black in here.")
        elif TheBridge.power_on == False:
            print("The only light seems to be coming from the alarm system.")
            print("Illuminating the room in a red light.")
        elif TheBridge.power_on:
            print("The floor lights are on.")
            print("looking around reveals sections of the ceiling had been on fire.")
            print("How long was i out for?")
        while True:
            print("What will you do?")
            choice = input("> ")
            if choice == "look left":
                print("There is a door with a sign [The Bridge]")
            elif choice == "go left":
                return 'The_bridge'
            elif choice == "go right":
                return 'Escape_pod'
            elif choice == "look right":
                print("There is a door with a sign [Armory]")
            else:
                print("I got no idea what that means.")
        pass

class LaserWeaponArmory(Scene):
    """
    Laser Weapon Armory This is where the hero gets a neutron bomb to blow
    up the ship before getting to the escape pod. It has a keypad the hero has to
    guess the number for """
    def enter(self):
        pass

class TheBridge(Scene):
    """ The Bridge Another battle scene with a Gothon where the hero places the
bomb."""

    alarm_off = False
    power_on = False
    def enter(Self):
        print("You enter [The bridge] ")
        if TheBridge.power_on == False:
            print("All the instruments seem to be off.")
        if TheBridge.alarm_off == False:
            print("The hellish blaring sound is going off and seems louder here.")
            print("The room is illuminated in red from the alarm lights.")
        while True:
            print("What will you do?")
            choice = input("> ")
            if choice == "help":
                print("look at <object>")
                print("look <direction>")
                print("use <object>")
            elif choice == "go back":
                return 'Central_corridor'
            elif choice == "look at alarm":
                if TheBridge.Alarm_off:
                    print("The yellow marked box on the wall is blinking in full force.")
                    print("After carefully opening the box, the panel reads: 2049.")
                    print("There seems to be a blue switch and red switch marked with symbols.")
                else:
                    print("The room is pitch black now....")
            elif choice == "use blue switch":
                print("You hear a low rattling noise.")
                print("There seems to be a flashing light behind you.")
                print("The screens of the bridge seem to be powering on.")
                print("After an audible thunk the lights come on.")
            elif choice == "use red switch":
                print("The siren slows down.")
                if TheBridge.power_on:
                    print("A voice comes on the intercome: Alarm override activated")
                    print("Crew members are mandated to investigate origins of alarm.")
                    print("To ensure vessel is still capable of the objective.")
                else:
                    print("Now with the noise off i can finally think.")
                    print("Although now the alarm lights are off it's really dark here.")
        pass

class EscapePod(Scene):
    """ Escape Pod Where the hero escapes but only after guessing the right escape
pod. """
    def enter(self):
        while True:
            print("What will you do?")
            choice = input("> ")
            if choice == "use escape pod":
                return('finished')
        pass

class Finish(Scene):
    def enter(self):
        print("Thanks for playing. You won")
        exit()

class Map(object):

    scenes = {
        'Central_corridor' : CentralCorridor(),
        'Laser_weapon_armory' : LaserWeaponArmory(),
        'The_bridge' : TheBridge(),
        'Escape_pod' : EscapePod(),
        'Death' : Death(),
        'finished' : Finish()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        pass

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        print(val)
        return val

    def opening_scene(self):
        print("You awake on the ground, there is a red pulsing light.")
        print("You get on one knee and notice a painfull pressure in your ears")
        print("In response you grab your nose and attempt to pop your eardrums")
        print("*POP*")
        print("The blaring siren is now hardly ignorable.")
        print("\'Where the fuck am i\'")
        print("With every rotation of the alarm light you can see a section of the corridor.")
        print("In flashing moments you realise your predicament and remember your training: ")
        print("In case of emergency escape pod!")
        return self.next_scene(self.start_scene)

a_map = Map('Central_corridor')
a_game = Engine(a_map)
a_game.play()
