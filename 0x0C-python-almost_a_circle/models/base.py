#!/usr/bin/python3
import json
import os.path
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        json_data = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(json_data))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        elif cls.__name__ == "Square":
            inst = cls(1)
        else:
            inst = None
        if inst:
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        file_name = f"{cls.__name__}.json"
        if not os.path.isfile(file_name):
            return []
        with open(file_name, "r") as file:
            json_data = file.read()
        dict_list = cls.from_json_string(json_data)
        return [cls.create(**inst) for inst in dict_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        try:
            csv_data = [obj.to_dictionary() for obj in list_objs]
        except FileNotFoundError:
            csv_data = []
        if not csv_data:
            return
        file_name = f"{cls.__name__}.csv"
        keys = csv_data[0].keys()
        with open(file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(csv_data)

    @classmethod
    def load_from_file_csv(cls):
        file_name = f"{cls.__name__}.csv"
        if not os.path.isfile(file_name):
            return []
        csv_data = []
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key, val in row.items():
                    try:
                        row[key] = int(val)
                    except ValueError:
                        pass
                csv_data.append(row)
        return [cls.create(**dic) for dic in csv_data]

