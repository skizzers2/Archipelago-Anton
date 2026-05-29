from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World

class AntonItem(Item):
    game = "ANTONBLAST"

# detonators should be event items?

item_name_to_id: dict[str, int] = {
    
}

def create_items(world: World):
    itempool = []