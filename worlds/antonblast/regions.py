from BaseClasses import Region, Entrance, CollectionRule, MultiWorld
from rule_builder.rules import True_
from locations import location_name_to_id, AntonLocation
from typing import List

pinball_mire_rooms: dict[str, tuple[List[str]|None, List[str]|None]] = { # Room Name: ([Locations], [Exits])
    "Gentle Wharf": (None, ["Hub"]),
    "Gimme A Hand!": (None, ["Gentle Wharf"]),
    "Shooting Range": (["Pinball Mire: Self Defense"], ["Gimme A Hand!"]),
    "Upward Climb": (None, ["Gimme A Hand!"]),
    "Pictures Of Home": (None, ["Upward Climb"]),
    "It's Inside The House": (None, ["Pictures Of Home"]),
    "The Great Excave": (None, ["It's Inside The House"]),
    "Cavern Catastrophe": (["Pinball Mire Casette"], ["The Great Excave"]),
    "Z-Axis": (None, ["Cavern Catastrophe"]),
    "Pinball Zone": (None, ["Z-Axis"]),
    "Funnel Up": (None, ["Pinball Zone"]),
    "Spruce Cadet": (["Pinball Mire: House Brew"], ["Funnel Up"]),
    "Antonball Room": (None, ["Spruce Cadet"]),
    "State Of Euphoria": (None, ["Antonball Room"]),
    "Tunnel Vision": (None, ["State of Euphoria"]),
    "Point Blank": (["Pinball Mire Spraycan"], ["Tunnel Vision"]),
    "Muddy Waters": (None, ["Tunnel Vision"]),
    "The Big Board": (None, ["Muddy Waters"]),
    "Rockslide Rumble": (["Pinball Mire Paul"], ["The Big Board"]),
    "Trickledown Blastonomics": (None, ["Rockslide Rumble"]),
    "Aaaahhhh!!!": (None, ["Trickledown Blastonomics"]),
    "Upward Climb (Escape)": (None, ["Aaaahhhh!!!"]),
    "Gimme A Hand! (Escape)": (None, ["Upward Climb (Escape)"]),
    "Gentle Wharf (Escape)": (["Pinball Mire Complete"], ["Gimme A Hand! (Escape)"])
}

def build_pinball_mire(multiworld: MultiWorld, player: int) -> List[Region]:
    def create_pinball_mire_room(room_name: str, locations: List[str]|None=None, exits: List[str]|None=None):
        new_reg = Region(room_name, player, multiworld, None)
        if locations != None:
            loc_map = {}
            for loc in locations:
                loc_map[loc] = location_name_to_id[loc]
            new_reg.add_locations(loc_map, AntonLocation)
        if exits != None:
            for k in exits:
                multiworld.get_region(k, player).connect(new_reg, None, True_) # define rules later, in a big dict
        return new_reg
    
    pinball_regions = []
    for k in pinball_mire_rooms.keys():
        pinball_regions.append(create_pinball_mire_room(k, pinball_mire_rooms[k][0], pinball_mire_rooms[k][1]))
    return pinball_regions
    

    
    


def create_regions(multiworld: MultiWorld, player: int):
    regions = []
    regions.append(Region("Hub", player, multiworld))
    regions += build_pinball_mire(multiworld, player)
    return regions