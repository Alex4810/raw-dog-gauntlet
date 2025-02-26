class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("You are dead.\n" +
                  "*RE4 Leon death sound*")
        else:
            print(f"{self.name} has {self.health} health remaining.")



