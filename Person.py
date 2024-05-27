class Person:
    def __init__(self, name, age):
        print("init")
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        self._age = value

    def __str__(self):
        return f"Person(name={self._name}, age={self._age})"
