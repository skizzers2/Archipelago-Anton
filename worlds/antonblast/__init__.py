from worlds.AutoWorld import World
from BaseClasses import ItemClassification
from . import locations, regions, items
import options as anton_options

class AntonWorld(World):
    """
    erm... what the blast
    """
    game = "ANTONBLAST"

    options_dataclass = anton_options.AntonOptions
    options: anton_options.AntonOptions

    origin_region_name = "Hub"

    item_name_to_id = items.item_name_to_id
    location_name_to_id = locations.location_name_to_id

    def create_regions(self) -> None:
        regions.create_regions()
    
    def set_rules(self) -> None:
        pass

    def create_items(self) -> None:
        items.create_items()

    def create_item(self, name: str) -> items.AntonItem:
        return items.AntonItem(name, ItemClassification.filler, items.item_name_to_id[name], self.player)
    
    def get_filler_item_name(self) -> str:
        return "DUMMY"