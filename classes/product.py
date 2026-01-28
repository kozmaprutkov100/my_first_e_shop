class Product:
    '''
    Класс Product
    Этим классом представлены товары в интернет магазине
    Метод __init__ :
    Конструктор инициализирует объект Product с двумя атрибутами: name (название товара) и price (цена товара).
    Пример: product1 = Product("Smartfone", 10000) создаст товар с название "Smartfone" и ценой 10000.
    Метод __str__:
    Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью команды print.
    Пример: print(product1) выведет " Продукт Smartfone, цена = 10000).
    '''
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"Продукт {self.name}, цена = {self.price})"