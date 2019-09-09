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
        self.scene_map.opening_scene(self.scene_map.scene_name)
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
    def enter(Self):
        pass

class EscapePod(Scene):
    """ Escape Pod Where the hero escapes but only after guessing the right escape
pod. """
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        self.scene_name = start_scene
        pass

    def next_scene(self, scene_name):
        #self.next_scene = scene_name
        pass

    def opening_scene(self):
        return self.scene_name

a_map = Map('Central_corridor')
a_game = Engine(a_map)
a_game.play()
