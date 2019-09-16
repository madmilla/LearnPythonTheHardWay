from nose.tools import *
from ex47.game import Room
from ex47.engine import Engine
from ex47.inventory import Item_list

def test_inventory_add_item():
	inv_a = Item_list()
	inv_a.addItem("FlashLight")
	assert_equal(inv_a.hasItem("FlashLight"), True)

def test_inventory_missing_item():
	inv_a = Item_list()
	assert_equal(inv_a.hasItem("Brick"), False)

def test_death():
	engine_a = Engine("Max Payne")
	assert_equal(engine_a.death(),"Max Payne")

def test_engine():
	engine_a = Engine("dev")
	assert_equal(engine_a.arg, "dev")

def test_room():
	gold = Room("GoldRoom",
		"""This room has gold in it you can grab.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})

def test_room_paths():
	center = Room("Center"," Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")

	center.add_paths({'north':north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)

def test_map():
	start = Room("Start", "You can go est and down a hole.")
	west = Room("Trees", "There are trees here, you can go")
	down = Room("Dungeon", "It's dark down here, you can go")

	start.add_paths({'west':west, 'down': down})
	west.add_paths({'east':start})
	down.add_paths({'up':start})

	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)

def setup():
	print("SETUP!")

def teardown():
	print("TEAR DOWN!")

def test_basic():
	print("I RAN!")
