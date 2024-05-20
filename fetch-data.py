import requests


def get_player_data(username):
    url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        return data
    else:
        print(f"Error: Unable to fetch data for {username}")
        return None


main_username = 'WasabiPengu'
skiller_username = 'BlossomXP'

main_data = get_player_data(main_username)
skiller_data = get_player_data(skiller_username)

print("Main Character Data: ")
print(main_data)

print("Skiller Character Data: ")
print(skiller_data)
