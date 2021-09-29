from World import World
from Foundation import Foundation


class Player(World, Foundation):
    def __init__(self, name, strength, agility, energy, talent, endurance, oxygen, gravity):
        super().__init__(oxygen, gravity)
        self.name = name
        self.strength = strength
        self.agility = agility
        self.energy = energy
        self.talent = talent
        self.endurance = endurance

    def endurance_test(self):
        Death = False
        breathe = True
        for i in range(1):
            if self.oxygen < 50:
                self.endurance -= 20

        if self.endurance <= 0:
            Death = True
            breathe = False

        if Death:
            return 'You have died'
            breathe = False
        else:
            return self.endurance


Player1 = Player('K1', 49, 12, 3, 25, 100, 49, 55)
print(Player1.endurance_test())
