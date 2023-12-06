# character.py
class Character:
    def __init__(self, name, width, height, speed):
        self.name = name
        self.width = width
        self.height = height
        self.speed = speed

characterValue = [
    Character(name="Basic", width=30, height=120, speed=10),
    Character(name="Fast", width=25, height=80, speed=15),
    Character(name="Slow", width=50, height=200, speed=5)
]