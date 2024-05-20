import pandas as pd
from io import StringIO

def parse_player_data(raw_data):
    skills = [
        "Overall", "Attack", "Defence", "Strength", "Hitpoints", "Ranged", "Prayer", "Magic",
        "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting",
        "Smithing", "Mining", "Herblore", "Agility", "Thieving", "Slayer", "Farming",
        "Runecrafting", "Hunter", "Construction"
    ]

    data = StringIO(raw_data)
    df = pd.read_csv(data, header=None, names=["Rank", "Level", "XP"])

    if len(df) < len(skills):
        missing_skills_count = len(skills) - len(df)
        missing_data = pd.DataFrame({
            "Rank": [None] * missing_skills_count,
            "Level": ["Unranked"] * missing_skills_count,
            "XP": [None] * missing_skills_count
        })
        df = pd.concat([df, missing_data], ignore_index=True)

    df.index = skills
    return df


# Sample data to test
sample_data = "1,99,13034431\n2,99,13034431\n"

parsed_data = parse_player_data(sample_data)
print(parsed_data)
