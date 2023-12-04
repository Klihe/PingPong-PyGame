# world.py
from modules.config import Config

class World:
    def __init__(self) -> None:
        self.config = Config()
        self.objects = []

    def addObject(self, object) -> None:
        self.objects.push(object)

    def getObjects(self) -> list:
        return self.objects

world = World()