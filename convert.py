import cc_dat_utils
import test_json_utils
import json
import cc_json_utils
#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
#print the resulting data
cc_dat = cc_dat_utils.make_cc_data_from_dat("data/intro.dat")
print(cc_dat)
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
#print(game_library)

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file
input_json_file = "data/zxiong_cc1.json"
with open(input_json_file, 'r') as reader:
    json_cc_data = json.load(reader)
cc_data_file = cc_json_utils.make_cc_data_file_from_json(json_cc_data)
#print(cc_data_file)

cc_dat_utils.write_cc_data_to_dat(cc_data_file, "data/zxiong_cc1.dat")

