class SuperHero:

    def __init__(self, sex, name, color):
        self.sex = sex
        self.name = name
        self.color = color
        self.head_count = 1
        self.hands_count = 2
        self.legs_count = 2
        self.say_hello()

    def say_hello(self):
        print(f"Супер герой {self.name} сказал вам привет!")

    def save_world(self):
        print(f"Супер герой  {self.name} спас мир")


class FlyingSuperHero(SuperHero):

    def fly(self):
        print(f"Супер герой  {self.name} пошел горизонтально летать")

    def get_info(self):
        print(f"Информация о летающем супергерое {self.name}")


class ChangedSuperHero(SuperHero):

    def self_change(self):
        print(f"Супер герой  {self.name} изменил свой облик")

    def get_info(self):
        print("Информация о изменяющийся супергерое")

class UnersalSuperHero(FlyingSuperHero, ChangedSuperHero):

    def __init__(self, sex, name, color, power):
        super().__init__(sex, name, color)
        self.power = power

    def fly(self):
        print(f"Супер герой  {self.name} пошел вертикально летать")

    def get_info(self):
        # ChangedSuperHero.get_info(self)
        super().get_info()
        print(f"Информация об универсальном супергерое {self.name}")



grutt = SuperHero("Male", "Grutt", "Wooden")
grutt.save_world()
grutt.say_hello()

spider_man = SuperHero("Male", "Peter Parker", "Red")
spider_man.save_world()

tor = FlyingSuperHero("Male", "Tor", "White")
tor.fly()

halk = ChangedSuperHero("Male", "Bruce Benner", "Green")
halk.self_change()

iron_man = UnersalSuperHero("Male", "Tony Stark", "Red/Gold", "universal")
iron_man.fly()
iron_man.self_change()
iron_man.get_info()


