class Warrier ():#Создали клаасс воина
    def __init__(self, name, power, endurance, hair_color):#Инициализируем атрибуты. Так это функция а внутри метод
        self.name = name #имя
        self.power = power #Сила
        self.endurance = endurance #Выносливость
        self.hair_color = hair_color #Цвет волос
    def sleep(self): #Метод для печати
        print(f'{self.name} лег спать')
        self.endurance += 2 #Увеличили выносливость

    def eat(self):
        print(f'{self.name} сел кушать')
        self.power += 2 #Увеличили силу

    def hit(self):
        print(f'{self.name} бьет кого-то')
        self.endurance -= 6#Уменьшили выносливость

    def walth(self):
        print(f'{self.name} гуляет')

    def info(self):
        print(f"Имя воина - {self.name}")
        print(f"Цыет волос воина - {self.hair_color}")
        print(f"Сила воина - {self.power}")
        print(f"Выносливость воина - {self.endurance}")
