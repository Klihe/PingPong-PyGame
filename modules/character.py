# character.py
class Character:
    def __init__(self, name, width, height, speed):
        self.name = name
        self.width = width
        self.height = height
        self.speed = speed

characterValue = [
    Character(name="Basic", width=30, height=120, speed=10),
    Character(name="Boosted", width=25, height=100, speed=15)
]