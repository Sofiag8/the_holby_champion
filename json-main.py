#!/usr/bin/python3
""" json main """


from base_champion import base_champion
from class_champion import champion

if __name__ == "__main__":

    champion1 = champion("Sakura", "Human", "Female")
    champion2 = champion("Yukito", "Elf", "Male")
    dictionary = champion.to_dictionary(champion1)
    json_dictionary = base_champion.to_json_string([dictionary])
    champion.save_information(champion, [champion1, champion2])
    print("This is the dictionary with the just created champion information:")
    print(dictionary)
    print("---------------------------------------------")
    print("This is the json dictionary:")
    print(json_dictionary)
    print("---------------------------------------------")
    with open("champion.json", "r") as file:
        print("---------------------------------------------")
        print("INFORMATION ABOUT THE TWO CREATED CHAMPIONS IN THE JSON FILE")
        print("----------------------------------------------")
        print(file.read())
    print("-----------------------------------------------")
    print("NOTES:")
    print("All the attributtes about experience and stats points are set to 0 because champions were just created, the general statistics are also set to 0 because at this point I haven't created the diferente champions classes")
