from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World
import json

class AntonItem(Item):
    game = "ANTONBLAST"

# detonators should be event items?

item_name_to_id: dict[str, int] = {
    # moves
    "Clutch":                                                        1,
    "Slide":                                                         2,
    "Hammer Vault":                                                  3,
    "Antomic Blast":                                                 4,
    "Swim Clutch":                                                   5,
    "Roll":                                                          6,

    # transfos
    "Sewer Shark":                                                   7,
    "Tornado":                                                       8,
    "Bomb":                                                          9,
    "Torpedo":                                                       10,
    "Pinball":                                                       11,
    "Segway":                                                        12,
    "Jetpack":                                                       13,
    "Ghost":                                                         14,
    "Chainsaw Mech":                                                 15,

    # levels
    "Boiler City":                                                   16,
    "Slowroast Sewer":                                               17,
    "Cinnamon Springs":                                              18,
    "Bomb Candy Mines":                                              19,
    "The Big Bath":                                                  20,
    "Concrete Jungle":                                               21,
    "Pinball Mire":                                                  22,
    "The Mad Mall":                                                  23,
    "Crimson Factory":                                               24,
    "The Mysterious Glasshouse":                                     25,
    "Devilled Gardens":                                              26,
    "Hell Manor":                                                    27,

    # bosses
    "Brawlbuster":                                                   28,
    "Tallbuster":                                                    29,
    "Smallbuster":                                                   30,
    "Maulbuster":                                                    31,
    "Jewel Ghoul":                                                   32,
    "Freako Dragon":                                                 33,
    "Ring-a-Ding":                                                   34,
    "Satan":                                                         35,

    # progression items
    "Spirit":                                                        36,
    "Progressive Health Upgrade":                                    37,
    "Satan Switch":                                                  38, # win condition
}

item_classifications: dict[str, ItemClassification] = {

}

def create_items(world: World):
    itempool = []