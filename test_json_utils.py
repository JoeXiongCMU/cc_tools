import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    #read the json file
    json_data = open(json_data, 'r').read()
    decoded_games = json.loads(json_data)
    print('DECODED:', decoded_games)

    for decoded_game in decoded_games:
        title = decoded_games[decoded_game]['title']
        year = decoded_games[decoded_game]['Year']

        platform_name = decoded_games[decoded_game]['platform']['name']
        platform_launch_year = decoded_games[decoded_game]['platform']['launch year']
        platform = test_data.Platform(name = platform_name, launch_year=platform_launch_year)

        game_library.games.append(test_data.Game(title=title, year=year, platform=platform))
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    #Return the completed game_library
    print(game_library)
    return game_library
