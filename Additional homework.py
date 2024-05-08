# Дополнительное задание:
# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store,
# который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# -  метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

class Store:
    def __init__(self, name, address, items):
        self.name = name
        self.address = address
        self.items = {} #Создаем пустой словарь для items
    def add_item(self, item, price): #Метод для добавления товара в ассортимент
        self.items[item] = price #Добавляем новый элемент в словарь

    def remove_item(self, item): #Метод для удаления товара из ассортимента
        if item in self.items: #Проверяем наличие элемента в словаре
            del self.items[item] #Удаляем элемент

    def get_price(self, item): #Метод для получения цены товара по его названию
        if item in self.items: #Проверяем наличие элемента в словаре
            return self.items[item] #Возвращаем цену
        else:
            return None

    def update_price(self, item, new_price): #Метод для обновления цены товара
        if item in self.items: #Проверяем наличие элемента в словаре
            self.items[item] = new_price #Обновляем цену

#Создание обьекта магазина
store1 = Store("Магазин 1", "Адрес магазина 1", {"apple": 0.5, "banana": 0.75})
store2 = Store("Магазин 2", "Адрес магазина 2", {"orange": 0.3, "milk": 1.5})
store3 = Store("Магазин 3", "Адрес магазина 3", {"bread": 0.8, "chocolate": 2.0})

print(store1.name, store1.address, store1.items)
print(store2.name, store2.address, store2.items)
print(store3.name, store3.address, store3.items)

#Добавление товара в ассортимент
store1.add_item("chocolate", 2.5)
store2.add_item("bread", 1.2)
store3.add_item("milk", 1.8)

print(store1.name, store1.address, store1.items)
print(store2.name, store2.address, store2.items)
print(store3.name, store3.address, store3.items)

#Удаление товара из ассортимента
store1.remove_item("chocolate")

print(store1.name, store1.address, store1.items)

#Получение цены товара по его названию
store2.get_price("bread")

print(store2.name, store2.address, store2.items)

#Обновление цены товара
store2.update_price("bread", 0.6)
store3.update_price("milk", 2.0)

print(store1.name, store1.address, store1.items)
print(store2.name, store2.address, store2.items)
print(store3.name, store3.address, store3.items)


