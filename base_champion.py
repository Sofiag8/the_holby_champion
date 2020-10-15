#!/usr/bin/python3
""" first champion class Base """
import json


class base_champion():
    """ champion base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ this is the initialization of champion base class
        """
        if id is not None:
            self.id = id
        else:
            base_champion.__nb_objects += 1
            self.id = base_champion.__nb_objects

    def to_json_string(champion_information):
        """ this method turns the champion object information to a
        JSON string
        """
        if champion_information is None or not champion_information:
            print("You have not created yet a champion")
            return
        return json.dumps(champion_information)

    def save_information(cls, list_obj):
        """ this method writes the JSON string representation of the
        champion information to a JASON file
        """
        empty_list = []
        filename = cls.__name__ + ".json"
        if list_obj is not None:
            empty_list = [i.to_dictionary() for i in list_obj]
        with open(filename, "w", encoding='utf-8') as file:
            file.write(cls.to_json_string(empty_list))

    def from_json_string(json_string):
        """ this method returns the string representation of the json file """
        if json_string is None or json_string is []:
            print("you did not save your champion information")
        return json.loads(json_string)
