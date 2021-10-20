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

        if Death:
            return 'You have died'

        else:
            return self.endurance

    def damage(self, strength):
        strength = self.strength
        Punch = True
        if Punch:
            strength *= 2
        return strength


Player1 = Player('K1', 9, 12, 3, 25, 100, 49, 55)
print(Player1.endurance_test())
print(Player1.damage(0))
