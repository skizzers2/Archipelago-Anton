from BaseClasses import Item, ItemClassification
from world import AntonWorld

class AntonItem(Item):
    game = "ANTONBLAST"

# detonators should be event items?

item_name_to_id: dict[str, int] = {
    "DUMMY": 1
}

def create_items(world: AntonWorld):
    itempool = []
    itempool += [world.create_filler() for _ in range(len(world.multiworld.get_unfilled_locations(world.player)))]
    world.multiworld.itempool += itempool
    