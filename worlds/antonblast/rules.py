from typing import List

anton_rooms: dict[str, dict] = { # Room Name: ([Locations], [Exits], [AccessRules])
    "Pinball Mire": {
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
        "Tunnel Vision": (None, ["State Of Euphoria"]),
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
}