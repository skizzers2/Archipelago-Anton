from worlds.AutoWorld import World
from BaseClasses import ItemClassification
from . import locations, regions, items
from .options import AntonOptions
from rule_builder.rules import CanReachLocation

class AntonWorld(World):
    """
    erm... what the blast
    """
    game = "ANTONBLAST"

    options_dataclass = AntonOptions
    options: AntonOptions

    origin_region_name = "Hub"

    topology_present = True

    item_name_to_id = items.item_name_to_id
    location_name_to_id = locations.location_name_to_id

    def create_regions(self) -> None:
        regions.create_regions(self)
    
    def set_rules(self) -> None:
        self.set_completion_rule(CanReachLocation("Pinball Mire Complete"))

    def create_items(self) -> None:
        items.create_items(self)

    def create_item(self, name: str) -> items.AntonItem:
        if name == "DUMMY2":
            return items.AntonItem(name, ItemClassification.progression, items.item_name_to_id[name], self.player)
        return items.AntonItem(name, ItemClassification.filler, items.item_name_to_id[name], self.player)