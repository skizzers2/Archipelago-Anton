from BaseClasses import Location
import json

class AntonLocation(Location):
    game = "ANTONBLAST"

anton_data = json.load(open("worlds/antonblast/data.json", "r"))

location_name_to_id: dict[str, int] = {
    # level spirits
    "Boiler City: Underground Brew":                                 1,
    "Slowroast Sewer: La Plunge":                                    2,
    "Cinnamon Springs: Tearri Tea":                                  3,
    "Bomb Candy Mines: Bombtail":                                    4,
    "The Big Bath: Crotch and Ankles":                               5,
    "Concrete Jungle: Mall Slop":                                    6,
    "Pinball Mire: House Brew":                                      7,
    "The Mad Mall: Shank Soda":                                      8,
    "Crimson Factory: Buppy Blast":                                  9,
    "The Mysterious Glasshouse: WTR...":                             10,
    "Devilled Gardens: Ponkler Seltzer":                             11,
    "Hell Manor: Devil's Brew":                                      12,

    # boss spirits
    "Brawlbuster: Brawlbrew":                                        13,
    "Jewel Ghoul: Jewel Brew":                                       14,
    "Tallbuster: Tallboy":                                           15,
    "Freako Dragon: Freak Drink":                                    16,
    "Smallbuster: Smallshot":                                        17,
    "Maulbuster: Maulvino":                                          18,
    "Ring-a-Ding: Hero of Wallowmere":                               19,

    # trash
    "Boiler City: Boob Tube":                                        20,
    "Slowroast Sewer: My Favorite Banana":                           21,
    "Cinnamon Springs: Shiny Foil":                                  22,
    "Bomb Candy Mines: Forgotten Toy":                               23,
    "The Big Bath: Pippogotchi":                                     24,
    "Concrete Jungle: Ahajsndio 64":                                 25,
    "Pinball Mire: Self Defense":                                    26,
    "The Mad Mall: Ballba Tea":                                      27,
    "Crimson Factory: Flumbo Kart":                                  28,
    "The Mysterious Glasshouse: Pride and Joy":                      29,
    "Devilled Gardens: Earmuffs":                                    30,
    "Hell Manor: Toy For Me":                                        31,

    # spraycans
    "Boiler City: Spraycan":                                         32,
    "Slowroast Sewer: Spraycan":                                     33,
    "Cinnamon Springs: Spraycan":                                    34,
    "Bomb Candy Mines: Spraycan":                                    35,
    "The Big Bath: Spraycan":                                        36,
    "Concrete Jungle: Spraycan":                                     37,
    "Pinball Mire: Spraycan":                                        38,
    "The Mad Mall: Spraycan":                                        39,
    "Crimson Factory: Spraycan":                                     40,
    "The Mysterious Glasshouse: Spraycan":                           41,
    "Devilled Gardens: Spraycan":                                    42,
    "Hell Manor: Spraycan":                                          43,

    # cassettes
    "Boiler City: Cassette":                                         44,
    "Slowroast Sewer: Cassette":                                     45,
    "Cinnamon Springs: Cassette":                                    46,
    "Bomb Candy Mines: Cassette":                                    47,
    "The Big Bath: Cassette":                                        48,
    "Concrete Jungle: Cassette":                                     49,
    "Pinball Mire: Cassette":                                        50,
    "The Mad Mall: Cassette":                                        51,
    "Crimson Factory: Cassette":                                     52,
    "The Mysterious Glasshouse: Cassette":                           53,
    "Devilled Gardens: Cassette":                                    54,
    "Hell Manor: Cassette":                                          55,

    # blue detonators
    "Boiler City: Blue Detonator":                                   56,
    "Slowroast Sewer: Blue Detonator":                               57,
    "Cinnamon Springs: Blue Detonator":                              58,
    "Bomb Candy Mines: Blue Detonator":                              59,
    "The Big Bath: Blue Detonator":                                  60,
    "Concrete Jungle: Blue Detonator":                               61,
    "Pinball Mire: Blue Detonator":                                  62,
    "The Mad Mall: Blue Detonator":                                  63,
    "Crimson Factory: Blue Detonator":                               64,
    "The Mysterious Glasshouse: Blue Detonator":                     65,
    "Devilled Gardens: Blue Detonator":                              66,
    "Hell Manor: Blue Detonator":                                    67,

    # green detonators
    "Boiler City: Green Detonator":                                  68,
    "Slowroast Sewer: Green Detonator":                              69,
    "Cinnamon Springs: Green Detonator":                             70,
    "Bomb Candy Mines: Green Detonator":                             71,
    "The Big Bath: Green Detonator":                                 72,
    "Concrete Jungle: Green Detonator":                              73,
    "Pinball Mire: Green Detonator":                                 74,
    "The Mad Mall: Green Detonator":                                 75,
    "Crimson Factory: Green Detonator":                              76,
    "The Mysterious Glasshouse: Green Detonator":                    77,
    "Devilled Gardens: Green Detonator":                             78,
    "Hell Manor: Green Detonator":                                   79,

    # red detonators
    "Boiler City: Red Detonator":                                    80,
    "Slowroast Sewer: Red Detonator":                                81,
    "Cinnamon Springs: Red Detonator":                               82,
    "Bomb Candy Mines: Red Detonator":                               83,
    "The Big Bath: Red Detonator":                                   84,
    "Concrete Jungle: Red Detonator":                                85,
    "Pinball Mire: Red Detonator":                                   86,
    "The Mad Mall: Red Detonator":                                   87,
    "Crimson Factory: Red Detonator":                                88,
    "The Mysterious Glasshouse: Red Detonator":                      89,
    "Devilled Gardens: Red Detonator":                               90,
    "Hell Manor: Red Detonator":                                     91,

    # yellow detonators
    "Boiler City: Yellow Detonator":                                 92,
    "Slowroast Sewer: Yellow Detonator":                             93,
    "Cinnamon Springs: Yellow Detonator":                            94,
    "Bomb Candy Mines: Yellow Detonator":                            95,
    "The Big Bath: Yellow Detonator":                                96,
    "Concrete Jungle: Yellow Detonator":                             97,
    "Pinball Mire: Yellow Detonator":                                98,
    "The Mad Mall: Yellow Detonator":                                99,
    "Crimson Factory: Yellow Detonator":                             100,
    "The Mysterious Glasshouse: Yellow Detonator":                   101,
    "Devilled Gardens: Yellow Detonator":                            102,
    "Hell Manor: Yellow Detonator":                                  103,

    # my wife is a great statistician
    "Boiler City: Danton":                                           104,
    "Slowroast Sewer: Danton":                                       105,
    "Cinnamon Springs: Danton":                                      106,
    "Bomb Candy Mines: Danton":                                      107,
    "Concrete Jungle: Danton":                                       108,
    "Pinball Mire: Danton":                                          109,
    "The Mad Mall: Danton":                                          110,
    "Crimson Factory: Danton":                                       111,
    "The Mysterious Glasshouse: Danton":                             112,

    # level completion
    "Boiler City: Complete":                                         113,
    "Slowroast Sewer: Complete":                                     114,
    "Cinnamon Springs: Complete":                                    115,
    "Bomb Candy Mines: Complete":                                    116,
    "The Big Bath: Complete":                                        117,
    "Concrete Jungle: Complete":                                     118,
    "Pinball Mire: Complete":                                        119,
    "The Mad Mall: Complete":                                        120,
    "Crimson Factory: Complete":                                     121,
    "The Mysterious Glasshouse: Complete":                           122,
    "Devilled Gardens: Complete":                                    123,
    "Hell Manor: Complete":                                          124,

    # paul
    "Boiler City: Paul":                                             125,
    "Slowroast Sewer: Paul":                                         126,
    "Cinnamon Springs: Paul":                                        127,
    "Bomb Candy Mines: Paul":                                        128,
    "The Big Bath: Paul":                                            129,
    "Concrete Jungle: Paul":                                         130,
    "Pinball Mire: Paul":                                            131,
    "The Mad Mall: Paul":                                            132,
    "Crimson Factory: Paul":                                         133,
    "The Mysterious Glasshouse: Paul":                               134,
    "Devilled Gardens: Paul":                                        135,
    "Hell Manor: Paul":                                              136,

    # par times
    "Boiler City: Par Time":                                         137,
    "Slowroast Sewer: Par Time":                                     138,
    "Cinnamon Springs: Par Time":                                    139,
    "Bomb Candy Mines: Par Time":                                    140,
    "The Big Bath: Par Time":                                        141,
    "Concrete Jungle: Par Time":                                     142,
    "Pinball Mire: Par Time":                                        143,
    "The Mad Mall: Par Time":                                        144,
    "Crimson Factory: Par Time":                                     145,
    "The Mysterious Glasshouse: Par Time":                           146,
    "Devilled Gardens: Par Time":                                    147,
    "Hell Manor: Par Time":                                          148,

    # combo chains
    "Boiler City: Combo Chain Complete":                             149,
    "Slowroast Sewer: Combo Chain Complete":                         150,
    "Cinnamon Springs: Combo Chain Complete":                        151,
    "Bomb Candy Mines: Combo Chain Complete":                        152,
    "The Big Bath: Combo Chain Complete":                            153,
    "Concrete Jungle: Combo Chain Complete":                         154,
    "Pinball Mire: Combo Chain Complete":                            155,
    "The Mad Mall: Combo Chain Complete":                            156,
    "Crimson Factory: Combo Chain Complete":                         157,
    "The Mysterious Glasshouse: Combo Chain Complete":               158,
    "Devilled Gardens: Combo Chain Complete":                        159,
    "Hell Manor: Combo Chain Complete":                              160,

    # CRACKED
    "Boiler City: CRACKED":                                          161,
    "Slowroast Sewer: CRACKED":                                      162,
    "Cinnamon Springs: CRACKED":                                     163,
    "Bomb Candy Mines: CRACKED":                                     164,
    "The Big Bath: CRACKED":                                         165,
    "Concrete Jungle: CRACKED":                                      166,
    "Pinball Mire: CRACKED":                                         167,
    "The Mad Mall: CRACKED":                                         168,
    "Crimson Factory: CRACKED":                                      169,
    "The Mysterious Glasshouse: CRACKED":                            170,
    "Devilled Gardens: CRACKED":                                     171,
    "Hell Manor: CRACKED":                                           172,

    # this jit cracks bosses
    "Brawlbuster: CRACKED":                                          173,
    "Tallbuster: CRACKED":                                           174,
    "Smallbuster: CRACKED":                                          175,
    "Maulbuster: CRACKED":                                           176,
    "Jewel Ghoul: CRACKED":                                          177,
    "Freako Dragon: CRACKED":                                        178,
    "Ring-a-Ding: CRACKED":                                          179,

    # lime trials
    "Lime Trial: Shark Tank":                                        180,
    "Lime Trial: Lime's a Beach":                                    181,
    "Lime Trial: Distilled Hill":                                    182,
    "Lime Trial: Rubble Rumble":                                     183,

    # shop locations; figure this out later
}