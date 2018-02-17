import cc_data
import json

def make_cc_data_file_from_json( json_data ):
    cc_data_file = cc_data.CCDataFile()

    for json_level in json_data:
        cc_level = cc_data.CCLevel()
        cc_level.level_number = json_level["level_number"]
        cc_level.time = json_level["time"]
        cc_level.num_chips = json_level["num_chips"]

        cc_level.upper_layer = json_level["upper_layer"]
        cc_level.lower_layer = json_level["lower_layer"]

        #Handle optional fields
        json_fields = json_level["optional_fields"]
        for json_field in json_fields:
            field_type = json_field["type"]
            if field_type == "title":
               # print("title field!")
                title = json_field["title"]
                cc_title_field = cc_data.CCMapTitleField(title)
                cc_level.add_field(cc_title_field)
            elif field_type == "hint":
               # print("hint field!")
                hint = json_field["hint"]
                cc_hint_field = cc_data.CCMapHintField(hint)
                cc_level.add_field(cc_hint_field)
            elif field_type == "password":
              #  print("password field!")
                password = json_field["password"]
                cc_password_field = cc_data.CCEncodedPasswordField(password)
                cc_level.add_field(cc_password_field)
            elif field_type == "monster":
              #  print("monster field!")
                monsters = json_field["monsters"]
                cc_monster_coordinate = []
                for monster in monsters:
                    cc_monster_coordinate.append(cc_data.CCCoordinate(monster[0], monster[1]))
                cc_monsters_field = cc_data.CCMonsterMovementField(cc_monster_coordinate)
                cc_level.add_field(cc_monsters_field)
            elif field_type == "clone_machines":
                clone_machines = json_field["clone_machines"]
                cc_machine = []
                for clone_machine in clone_machines:
                    bx = clone_machine["button_coord"][0]
                    by = clone_machine["button_coord"][1]
                    tx = clone_machine["machine_coord"][0]
                    ty = clone_machine["machine_coord"][1]
                    cc_machine.append(cc_data.CCCloningMachineControl(bx, by, tx, ty))
                cc_clone_machine_field = cc_data.CCCloningMachineControlsField(cc_machine)
                cc_level.add_field(cc_clone_machine_field)
            elif field_type == "traps":
                traps = json_field["traps"]
                cc_trap = []
                for trap in traps:
                    bx = trap["button_coord"][0]
                    by = trap["button_coord"][1]
                    tx = trap["trap_coord"][0]
                    ty = trap["trap_coord"][1]
                    cc_trap.append(cc_data.CCTrapControl(bx, by, tx, ty))
                cc_trap_field = cc_data.CCTrapControlsField(cc_trap)
                cc_level.add_field(cc_trap_field)
            else:
                print("no other field")

        print(cc_level)
        cc_data_file.add_level(cc_level)

    return cc_data_file