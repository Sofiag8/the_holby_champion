#!/usr/bin/python3
""" class Rectangle """
from base_champion import base_champion


class champion(base_champion):
    """ champion inherited from the base_champion class
    with id and number of objects (champions created) """
    def __init__(self, name="", race="", gender="", level=0, exp_next_level=100,
                 current_exp=0, total_exp=0, stats={'Health': 0, 'Attack': 0, 'Defense': 0, 'Magic': 0, 'Speed': 0}, stat_points=0, id=None):
        """ this is the initialization of the champion class

        Args:
            Name (str):  Can be any combination of 10 Unicode characters

            Race (str): the user can choose Human, Elf, Dwarf,
            Hobbit, Orc (Only 1)

            Gender (str): the user can choose Male, Female, Other
            (Only 1)

            level (int): Starts at 0 and can go up to 100

            exp_next_level (int):  The amount of experience
            needed to reach the next level.

            current_exp (int):The amount of EXP our hero has in
            the current level

            total_exp (int): The amount of EXP our hero/heroine has in
            total from all levels. (Positive)

            stats (dict): should contain key/value about Health, Attack,
            Defense, Magic, Speed (all of them)

            stat_points (int): A certain number of points that can be
            used to increase any stat of our character. (Positive)
        """
        super().__init__(id)  # Call super class with id __init__ Base logic
        self.name = name
        self.race = race
        self.gender = gender
        self.level = level
        self.exp_next_level = exp_next_level
        self.current_exp = current_exp
        self.total_exp = total_exp
        self.stats = stats
        self.stat_points = stat_points


    def level_up(self):
        """ Method that allows to the champion level up after
        certain amount of EXP, increasing his/her level value and gaining
        3 stats points. Here (everytime the champion level up) tje current
        EXP is reset to 0, EXP for next level is set and total EXP is increased
        """
        if self.current_exp == self.exp_next_level:
            self.level += 1
            self.stat_points += 3
            self.current_exp = 0
            self.exp_next_level = 100
            self.total_exp += 25
            return (self)

    def gain_exp(self):
        """ This method increases the champion current EXP """

    def death(self):
        """ Method death. If champion dies, he/she loses 50% of the current
        experience """

    def increase_stats(self):
        """ uses a dictionary (method update stats) to update stats based of
        the amount of stat points the champion currently has """
        if current_exp == 100:
            update_stats(self)

    def update_stats(self):
        """ stats update method, incremeting by 3 according to the stats points
        the champion has"""
        if "Attack" in self.stats:
            self.stats["Attack"] += 3
        if "Defense" in self.stats:
            self.stats["Defense"] += 3
        if "Magic" in self.stats:
            self.stats["Magic"] += 3
        return self.stats

    def to_dictionary(self):
        """ this is a method definition that creates a dictionary
        with all the created champion information, so we can later
        create the json file
        """
        return {"id": self.id, "name": self.name, "race": self.race,
                "gender": self.gender, "level": self.level,
                "Experience needed for next level": self.exp_next_level,
                "current experience of the champion": self.current_exp,
                "total experience of the champion": self.total_exp,
                "general champion statistics": self.stats,
                "plus statistics points": self.stat_points}

    """ json-main allows to create in this case 2 champions and write and read a
    json file """

    """ At this point I'm missing the creation of the champion classes such as
    cleric, mage, paladin, figther, range and rogue, where the general
    statistics (stats) will be set, also we are missing the general methods for
    the base_champions about how experience and level increase, AND the elements
    (subclasses) for each champion class (fire, ice, and void """
