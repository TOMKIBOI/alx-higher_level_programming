#!/usr/bin/python3
"""
Write a class Student that defines a student by: (based on 10-student.py)
"""


class Student():
    """
        a class Student that defines a student by: (based on 10-student.py)
    """
    def __init__(self, first_name, last_name, age):
        """
            Instantiation with
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves a dictionary representation
            of a Student instance
        """
        if type(attrs) is list and all([type(j) == str for j in attrs]):
            return {k: l for k, l in self.__dict__.items() if k in attrs}
        return (self.__dict__)

    def reload_from_json(self, json):
        """
             replaces all attributes of the Student instance
        """
        for m, n in json.items():
            self.__dict__[m] = n
