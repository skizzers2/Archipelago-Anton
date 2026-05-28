from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World

class AntonItem(Item):
    game = "ANTONBLAST"

# detonators should be event items?

item_name_to_id: dict[str, int] = {
    "DUMMY1": 1,
    "DUMMY2": 2
}

def create_items(world: World):
    itempool = []
    world.multiworld.itempool.append(world.create_item("DUMMY2"))
    itempool += [world.create_item("DUMMY1") for _ in range(len(world.multiworld.get_unfilled_locations(world.player)))]
    world.multiworld.itempool += itempool
    