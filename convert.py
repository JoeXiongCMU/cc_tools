import cc_dat_utils
import test_json_utils
#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
#print the resulting data
cc_dat = cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat")
#print(cc_dat)
#print("data/pfgd_test.dat")



#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
### End Add Code Here ###
game_library = test_json_utils.make_game_library_from_json(input_json_file)
print("END!!!!!")
#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file