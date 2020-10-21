#!/usr/bin/python3
""" json main """


from base_champion import base_champion
from class_champion import champion

if __name__ == "__main__":

    print("MODE")
    print("1 Player")
    print("2 Players")
    print("Multiplayer")
    mode = input("Choose mode: ")
    """----------------------------------------------------------------------"""
    if mode == "1 Player":
        """ USER information """
        name = input("Enter your hero's name: ")
        if len(name) > 10:
            print("Please no more than 10 characters")
            name = input("Enter your hero's name: ")
        race = input("Write {}'s race (Human, Elf, Dwarf, Hobbit, Orc): ".format(name))
        if len(race) > 6:
            print("Just one race allowed")
            race = input("Write {}'s race (Human, Elf, Dwarf, Hobbit, Orc): ".format(name))
            if len(race) < 3:
                print("Choose an existent race")
                race = input("Write {}'s race (Human, Elf, Dwarf, Hobbit, Orc): ".format(name))
        gender = input("{} is it Female or Male: ".format(name))
        if len(gender) < 4 or len(gender) > 6:
            print("Choose a valid gender for {}".format(name))
            gender = input("{} is it Female or Male: ".format(name))

        """ creating champions """
        champion1 = champion(name, race, gender)
        """ About saving and loading champions information """
        dictionary = champion.to_dictionary(champion1)
        json_dictionary = base_champion.to_json_string([dictionary])
        champion.save_information(champion, [champion1])
        print("LOADING INFORMATION...")
        print(dictionary)
        print("---------------------------------------------")
        print("SAVED INFORMATION FOR {}:".format(name))
        print(json_dictionary)
        print("---------------------------------------------")
        with open("champion.json", "r") as file:
            print("---------------------------------------------")
            print("INFORMATION ABOUT THE TWO CREATED CHAMPIONS IN THE JSON FILE")
            print(" ")
            print(file.read())
    """----------------------------------------------------------------------"""
    if mode == "2 Players":
        """ USER information """
        name_player_1 = input("Enter first player hero's name: ")
        if len(name_player_1) > 10:
            print("Please no more than 10 characters")
            name_player_1 = input("Enter first player hero's name: ")
        name_player_2 = input("Enter second player hero's name: ")
        if len(name_player_2) > 10:
            print("Please no more than 10 characters")
            name_player_2 = input("Enter second player hero's name: ")

        race_player_1 = input("Write {}'s race (Human, Elf, Dwarf, Hobbit, Orc): ".format(name_player_1))
        if len(race_player_1) > 6:
            print("Just one race allowed")
            race_player_1 = input("Write {}'s race (Human, Elf, Dwarf, Hobbit, Orc): ".format(name_player_1))
            if len(race_player_1) < 3:
                print("Choose an existent race")
                race_player_1 = input("Write {} race (Human, Elf, Dwarf, Hobbit, Orc): ".format(name_player_1))

        race_player_2 = input("Write {}'s race (Human, Elf, Dwarf, Hobbit, Orc): ".format(name_player_2))
        if len(race_player_2) > 6:
            print("Just one race allowed")
            race_player_2 = input("Write {}'s race (Human, Elf, Dwarf, Hobbit, Orc): ".format(name_player_2))
        if len(race_player_2) < 3:
            print("Choose an existent race")
            race_player_2 = input("Write {}'s race (Human, Elf, Dwarf, Hobbit, Orc): ".format(name_player_2))
        gender_player_1 = input("{} is it Female or Male: ".format(name_player_1))
        if len(gender_player_1) < 4 or len(gender_player_1) > 6:
            print("Choose a gender for your {}: ".format(name_player_1))
            gender_player_1 = input("{} is it Female or Male: ".format(name_player_1))

        gender_player_2 = input("{} is it Female or Male: ".format(name_player_2))
        if len(gender_player_2) < 4 or len(gender_player_2) > 6:
            print("Choose a gender for your {}: ".format(name_player_2))
            gender_player_2 = input("{} is it Female or Male: ".format(name_player_2))

            """ creating champions """
        champion1 = champion(name_player_1, race_player_1, gender_player_1)
        champion2 = champion(name_player_2, race_player_2, gender_player_2)
        """ About saving and loading champions information """
        dictionary = champion.to_dictionary(champion1)
        dictionary2 = champion.to_dictionary(champion2)
        json_dictionary = base_champion.to_json_string([dictionary])
        json_dictionary2 = base_champion.to_json_string([dictionary2])
        champion.save_information(champion, [champion1, champion2])
        print("LOADING INFORMATION")
        print(dictionary)
        print(dictionary2)
        print("---------------------------------------------")
        print("SAVED INFORMATION FOR {}:".format(name_player_1))
        print(json_dictionary)
        print("SAVED INFORMATION FOR {}:".format(name_player_2))
        print(json_dictionary2)
        print("---------------------------------------------")
        with open("champion.json", "r") as file:
            print("---------------------------------------------")
            print("INFORMATION ABOUT THE TWO CREATED CHAMPIONS IN THE JSON FILE")
            print(" ")
            print(file.read())


    """ NOTES
    All the attributtes about experience and stats points are set to 0 because
    champions were just created, the general statistics are also set to 0
    because I haven't created the diferente champions classes """
