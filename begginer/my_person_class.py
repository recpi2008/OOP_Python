class Person:
    hands_count = 2
    legs_count = 2
    sex = None

    def __init__(self, sex, eye_color, hair_color, height, weight):
        self.sex = sex
        self._eye_color = eye_color
        self._hair_color = hair_color
        self.__height = height
        self.__weight = weight
        self.hair_len = None
        print("Создан новый объект класса Person")

    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        self.__height = new_height

    def get_sex(self):
        print("Sex of this person:", self.sex)
        self.get_eye_color()

    def get_eye_color(self):
        print("Eye color of this person", self._eye_color)

    def get_hair(self, hair_len):
        self.hair_len = hair_len
        print(f"Person has hair {self._hair_color} color of len {hair_len}")

    def go_to_eat(self):
        print("Person goes to eat")

    def go_to_sleep(self):
        print("Person goes to sleep")

    def wake_up(self):
        print("Person wakes up")


class WorkingPerson(Person):
    def __init__(self, sex, eye_color, hair_color, height, weight, working_hours):
        super().__init__(sex, eye_color, hair_color, height, weight)
        self.working_hours = working_hours
        print("Создан новый объект класса Working Person")

    def go_to_work(self):
        print(f"Person goes to work for {self.working_hours} hours")

    def get_info(self):
        print("This person is working person")

    def go_to_sleep(self, sleep_hours):
        print(f"Person goes to sleep for {sleep_hours} hours")


class HomeStayPerson(Person):
    def __init__(self, sex, eye_color, hair_color, height, weight):
        super().__init__(sex, eye_color, hair_color, height, weight)
        print("Создан новый объект класса Home Stay Person")

    def go_to_wash_dish(self):
        print("Person goes to wash the dish")

    def go_to_cook(self):
        print("Person cooks the dinner")

    def get_info(self):
        print("This person is homestay person")


class UniversalPerson(WorkingPerson, HomeStayPerson):
    def __init__(self, sex, eye_color, hair_color, height, weight, working_hours):
        super().__init__(sex, eye_color, hair_color, height, weight, working_hours)
        print("Создан новый объект класса UniversalPerson")

    def get_info(self):
        print("This person is universal person")

    def go_to_cook(self, food_type):
        print(f"Person eats {food_type}")


first_person = Person("Male", "blue", "black", 170, 60)
second_person = WorkingPerson("Female", "brown", "brown", 160, 52, 7)
second_person.get_eye_color()

third_person = HomeStayPerson("Female", "blue", "red", 175, 60)
third_person.wake_up()
third_person.go_to_cook()
third_person.go_to_eat()

fourth_person = UniversalPerson("Female", "brown", "brown", 160, 52, 7)
fourth_person.wake_up()
fourth_person.go_to_cook("MacDonalds")
fourth_person.go_to_eat()
fourth_person.go_to_work()
fourth_person.get_info()
fourth_person.go_to_sleep(7)


