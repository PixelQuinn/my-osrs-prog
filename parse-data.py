import pandas as pd
from io import StringIO


def parse_player_data(raw_data):
    data = StringIO(raw_data)
    df = pd.read_csv(data, header=None)
    df.columns = [
        "Overall Rank", "Overall Level", "Attack Rank", "Attack Level", "Attack XP", "Defensive Rank", "Defensive Level",
        "Defensive XP", "Strength Rank", "Strength Level", "Strength XP", "Hitpoints Rank", "Hitpoints Level",
        "Hitpoints XP", "Ranged Rank", "Ranged Level", "Ranged XP", "Prayer Rank", "Prayer Level", "Prayer XP",
        "Magic Rank", "Magic Level", "Magic XP", "Cooking Rank", "Cooking Level", "Cooking XP", "Woodcutting Rank",
        "Woodcutting Level", "Woodcutting XP", "Fletching Rank", "Fletching Level", "Fletching XP", "Fishing Rank",
        "Fishing Level", "Fishing XP", "Firemaking Rank", "Firemaking Level", "Firemaking XP", "Crafting Rank",
        "Crafting Level", "Crafting XP", "Smithing Rank", "Smithing Level", "Smithing XP", "Mining Rank", "Mining Level",
        "Mining XP", "Herblore Rank", "Herblore Level", "Herblore XP", "Agility Rank", "Agility Level", "Agility XP",
        "Thieving Rank", "Thieving Level", "Thieving XP", "Slayer Rank", "Slayer Level", "Slayer XP", "Farming Rank",
        "Farming Level", "Farming XP", "Runecraft Rank", "Runecraft Level", "Runecraft XP", "Huntering Rank",
        "Hunter Level", "Hunter XP", "Construction Rank", "Construction Level", "Construction XP"
    ]
    return df


# Sample date for testing
# sample_data = "1, 99, 13034431\n2, 99, 13034431\n"

# parsed_data = parse_player_data(sample_data)
# print(parsed_data)