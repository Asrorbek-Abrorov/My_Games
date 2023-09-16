import random


class Gun:
    def __init__(self, name, cost, damage):
        self.name = name
        self.cost = cost
        self.damage = damage


class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.gun = None

    def attack(self, player):
        player.health -= 10
        return f"attacked"


class Terrorist(Player):
    def __init__(self, name, health, money):
        super().__init__(name, health)
        self.money = money

    def buy(self, guns, default):
        for gun in guns:
            if self.money >= gun.cost:
                self.money -= gun.cost
                self.gun = gun
                print(f"{self.name} bought {self.gun.name}")
                break
        else:
            self.gun = default
            print(f"{self.name} doesn't have enough money")

    def attack(self, player):
        if not isinstance(player, Terrorist):
            if self.gun is not None:
                player.health -= self.gun.damage
                print(f"{self.name} attacked {player.name}")
            else:
                player.health -= 10
            if player.health <= 0:
                self.money += 1000
                print(f"{player.name} died")
                return True
            return False


class CounterTerrorist(Player):
    def __init__(self, name, health, money):
        super().__init__(name, health)
        self.money = money

    def buy(self, guns, default):
        for gun in guns:
            if self.money >= gun.cost:
                self.money -= gun.cost
                self.gun = gun
                print(f"{self.name} bought {self.gun.name}")
                break
        else:
            self.gun = default
            print(f"{self.name} doesn't have enough money")

    def attack(self, player):
        if not isinstance(player, CounterTerrorist):
            if self.gun is not None:
                player.health -= self.gun.damage
                print(f"{self.name} attacked {player.name}")
            else:
                player.health -= 10
            if player.health <= 0:
                self.money += 1000
                print(f"{player.name} died")
                return True
            return False


ak47 = Gun("ak47", 2700, 35)
awp = Gun("awp", 4750, 100)
m21 = Gun("m21", 2700, 70)
m4a1 = Gun("m4a1", 2700, 35)
shotgun = Gun("shotgun", 2700, 50)
Pulyimot = Gun("Pulyimot", 2700, 50)
Nova = Gun("Nova", 1200, 26)
mag7 = Gun("mag7", 1300, 30)
XM1014 = Gun("XM1014", 2000, 25)
PP_Bizon = Gun("PP-Bizon", 1400, 27)
FAMAS = Gun("FAMAS", 2050, 30)

guns = [ak47, awp, m21, m4a1, shotgun, Pulyimot, Nova, mag7, PP_Bizon, FAMAS]

usp = Gun("usp", 0, 15)
glock = Gun("glock", 0, 10)

player1 = CounterTerrorist("Asror", 100, 10000)
player2 = Terrorist("Asilbek", 100, 10000)
player3 = CounterTerrorist("Javohir", 100, 10000)
player4 = Terrorist("Dadajon", 100, 10000)

players = [player1, player2, player3, player4]

rounds = 0
wins_ct = [0, 0]

while rounds != 3:
    random.shuffle(guns)
    player1.buy(guns, usp)

    random.shuffle(guns)
    player2.buy(guns, glock)

    random.shuffle(guns)
    player3.buy(guns, usp)

    random.shuffle(guns)
    player4.buy(guns, glock)

    ct1, ct2, t1, t2 = False, False, False, False

    while player1.health > 0 and player2.health > 0 and player3.health > 0 and player4.health > 0:
        random.shuffle(players)
        attacker = players[0]
        if isinstance(attacker, CounterTerrorist):
            if player2.health > 0:
                ct1 = attacker.attack(player2)
            if player4.health > 0:
                ct2 = attacker.attack(player4)
        elif isinstance(attacker, Terrorist):
            if player1.health > 0:
                t1 = attacker.attack(player1)
            if player3.health > 0:
                t2 = attacker.attack(player3)

    print()
    print(f"{player1.name} {player1.health} {player1.money}")
    print(f"{player2.name} {player2.health} {player2.money}")
    print(f"{player3.name} {player3.health} {player3.money}")
    print(f"{player4.name} {player4.health} {player4.money}")
    print()

    if ct1 or ct2:
        wins_ct[0] += 1
        player2.health = 100
        player4.health = 100
        player2.money += 2000
        player4.money += 2000
    elif t1 or t2:
        wins_ct[1] += 1
        player1.health = 100
        player3.health = 100
        player1.money += 2000
        player3.money += 2000

    for player in players:
        player.money += 1000
        player.health = 100

    rounds += 1

print(f"Counter Terrorists: {wins_ct[0]} wins")
print(f"Terrorists: {wins_ct[1]} wins")
